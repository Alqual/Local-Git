package main

import "fmt"

func main() {
	var N, count int
	var S string
	fmt.Scan(&N, &S)
	var maps map[byte]int = map[byte]int{}
	for i := 1; i < N; i++ {
		if S[i] == S[i-1] {
			if maps[S[i]] == 0 {
				maps[S[i]] = 2
			} else {
				maps[S[i]]++
			}
		}
	}
	for _, v := range maps {
		count += v * (v - 1) / 2
	}
	fmt.Println(count)
}
