package main

import "fmt"

func main() {
	var N, K, R, S, P int
	var T string
	fmt.Scan(&N, &K)
	fmt.Scan(&R, &S, &P)
	fmt.Scan(&T)
	var ans int
	chk := make([]int, N)
	var score map[string]int = map[string]int{"r": P, "s": R, "p": S}
	for i := 0; i < N; i++ {
		//fmt.Println(i, T[i], string(T[i]), score[string(T[i])], ans)
		if i < K {
			ans += score[string(T[i])]
			chk[i] = 1
		} else {
			if T[i] != T[i-K] {
				ans += score[string(T[i])]
				chk[i] = 1
			} else {
				if i < 2*K {
					chk[i] = -1
					chk[i-K] = 1
				} else if chk[i-K] == 1 {
					chk[i] = -1
				} else {
					ans += score[string(T[i])]
					chk[i] = 1
				}
			}
		}
	}
	fmt.Println(ans)
}
