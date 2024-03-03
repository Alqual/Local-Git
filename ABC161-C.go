package main

import "fmt"

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func main() {
	var N, K int
	fmt.Scan(&N, &K)
	if N < K {
		fmt.Println(min(N, K-N))
	} else {
		fmt.Println(min(N%K, K-N%K))
	}
}
