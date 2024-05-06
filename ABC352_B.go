package main

import "fmt"

func main() {
	var S, T string
	fmt.Scan(&S)
	fmt.Scan(&T)
	var ans []int = []int{}
	var j int = 0
	for i := 0; i < len(S); i++ {
		for j < len(T) {
			if S[i] == T[j] {
				ans = append(ans, j+1)
				j++
				break
			}
			j++
		}
	}
	for _, i := range ans {
		fmt.Print(i, " ")
	}
}
