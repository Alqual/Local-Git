package main

import "fmt"

func main() {
	var A1, A2, A3 int
	fmt.Scan(&A1, &A2, &A3)
	if A2-A1 == A3-A2 {
		fmt.Println(0)
	} else {
		if A2-A1 < A3-A2 {
			d := (A3 - A2 - (A2 - A1))
			if d%2 == 0 {
				fmt.Println(d / 2)
			} else {
				fmt.Println(d/2 + 2)
			}
		} else {
			d := (A2 - A1 - (A3 - A2))
			fmt.Println(d)
		}
	}
}
