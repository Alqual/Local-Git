package main

import "fmt"

func main() {
	var S string
	fmt.Scan(&S)
	var c int
	for i := 0; i < len(S); i++ {
		if S[i] == '|' {
			if c == 0 {
				c = i + 1
			} else {
				fmt.Println(string(S[:c-1]) + string(S[i+1:]))
				break
			}
		}
	}
}
