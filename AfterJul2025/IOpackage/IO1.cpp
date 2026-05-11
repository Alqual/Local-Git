#include <iostream>
#include <vector>
#include <string>
#include <fcntl.h>
#include <unistd.h>
#include <liburing.h>
#include <stdexcept>

//この「同期的ラッパー」の核心は、**「要求を1つ発行して、それが完了するまで即座に待つ」**という処理をカプセル化することです。liburingライブラリには、まさにこのためのio_uring_submit_and_wait()という便利な関数が用意されています。

// これにより、非同期I/Oの利点を享受しつつ、コードの見た目は同期的なものになります。

// RAIIでio_uringのセットアップとクリーンアップを管理するクラス
class UringSync {
private:
    struct io_uring ring;

public:
    UringSync() {
        if (io_uring_queue_init(8, &ring, 0) < 0) {
            throw std::runtime_error("io_uring_queue_init failed");
        }
    }

    ~UringSync() {
        io_uring_queue_exit(&ring);
    }

    // 同期的なread処理を行うラッパー関数
    ssize_t read_sync(int fd, void *buffer, size_t size) {
        struct io_uring_sqe *sqe = io_uring_get_sqe(&ring);
        if (!sqe) {
            return -1; // Submission queue is full
        }

        // 1. 読み取り要求を作成する
        io_uring_prep_read(sqe, fd, buffer, size, 0);

        // 2. 要求をカーネルに発行し、完了するまで待機する
        if (io_uring_submit_and_wait(&ring, 1) < 0) {
            return -1; // Submit failed
        }

        // 3. 完了キューから結果を取得する
        struct io_uring_cqe *cqe;
        io_uring_peek_cqe(&ring, &cqe);
        if (!cqe) {
            return -1; // Should not happen after waiting
        }

        ssize_t result = cqe->res;
        io_uring_cqe_seen(&ring, cqe); // 結果を処理済みとしてマーク

        return result;
    }
};

int main() {
    const char* filename = "test.txt";
    // テスト用のファイルを作成
    int fd_w = open(filename, O_WRONLY | O_CREAT | O_TRUNC, 0644);
    write(fd_w, "Hello, Synchronous io_uring!", 28);
    close(fd_w);

    try {
        UringSync uring;
        std::vector<char> buffer(1024);

        int fd = open(filename, O_RDONLY);
        if (fd < 0) {
            perror("open");
            return 1;
        }

        std::cout << "Reading file with synchronous io_uring wrapper..." << std::endl;

        // 見た目は完全に同期的なread呼び出し
        ssize_t bytes_read = uring.read_sync(fd, buffer.data(), buffer.size());

        if (bytes_read < 0) {
            std::cerr << "Read failed: " << strerror(-bytes_read) << std::endl;
        } else {
            std::cout << "Read " << bytes_read << " bytes: " << std::string(buffer.data(), bytes_read) << std::endl;
        }

        close(fd);

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    
    unlink(filename); // テストファイルを削除
    return 0;
}