package main

import "fmt"

func max(x, y int) int {
	if x < y {
		return y
	}
	return x
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func main() {
	var N, X, Y, Z int
	fmt.Scan(&N, &X, &Y, &Z)
	if min(X, Y) > Z || max(X, Y) < Z {
		fmt.Println("No")
	} else {
		fmt.Println("Yes")
	}
}
