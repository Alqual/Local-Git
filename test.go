package main

import "fmt"

func calc(x, y int) int {
	var z int
	z = x + y
	return z
}

func main() {
	fmt.Print("hello")
	fmt.Print(calc(1, 2))
}
