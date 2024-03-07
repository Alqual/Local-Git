package main

import "fmt"

func main() {
	var X, c int
	fmt.Scan(&X)
	c = 2
	for c*c < X {
		if X%c == 0 {
			X++
			c = 2
		} else {
			c++
		}
	}
	fmt.Println(X)

}
