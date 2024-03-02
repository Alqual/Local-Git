package main

import "fmt"

func main() {

	var a, b int
	fmt.Scan(&a, &b)
	for i := 0; i < 10; i++ {
		if i != a+b {
			fmt.Println(i)
			break
		}
	}
}
