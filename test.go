package main

import "fmt"

"github.com/Alqual/Local-Git")

func calc(x, y int) int {
	var z int
	z = x + y*y
	return z
}

func mod(x, y int) int {
	var z int
	z = x % y
	return z
}

func sub(x, y int) int {
	var z int
	z = x - y
	return z
}

func main() {
	fmt.Print("hello")
	fmt.Print(calc(1, 2))
	fmt.Print(mod(1, 2))
}
