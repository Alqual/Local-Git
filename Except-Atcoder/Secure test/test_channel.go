package main

import "fmt"

// 2, 3, 4, 5...と自然数を送信するチャネルを作る
func generate(ch chan<- int) {
	for i := 2; ; i++ {
		ch <- i
	}
}

// srcチャネルから送られてくる値の中で、primeの倍数でない値だけをdstチャネルに送信する関数
func filter(src <-chan int, dst chan<- int, prime int) {
	for i := range src {
		if i%prime != 0 {
			dst <- i
		}
	}
}

// エラトステネスのふるいのアルゴリズム本体
func sieve() {
	ch := make(chan int)
	go generate(ch)
	for {
		prime := <-ch // ここから受け取るものは素数で確定
		fmt.Print(prime, "\n")

		// 素数と確定した数字の倍数は
		// もう送ってこないようなチャネルを新規作成→chに代入
		ch1 := make(chan int)
		go filter(ch, ch1, prime)
		ch = ch1
	}
}

func main() {
	sieve()
}
