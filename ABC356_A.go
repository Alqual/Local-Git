package main

import "fmt"

func main() {
	var N, L, R int
	fmt.Scan(&N, &L, &R)
	ans := make([]int, N)
	for i := 0; i < N; i++ {
		if i <= L-2 || i >= R {
			ans[i] = i + 1
		} else {
			ans[i] = R - (i - L + 1)
		}
	}
	for i := 0; i < N; i++ {
		fmt.Print(ans[i], " ")
	}
}
