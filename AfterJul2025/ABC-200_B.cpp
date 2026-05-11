#include <iostream>
using namespace std;

int main() {
    int N, K,W;
    W = 200;
    string DK;
    std::cin >> N>>K;
    for (int i =1; i<K+1; i++) {
        if (N % W == 0) {
            N /= W;
        } else  {
            DK = to_string(N)+"200";
            N= stoi(DK);
        }
    }
        std::cout << N << std::endl;
    }
