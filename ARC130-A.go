package main

import (
	"fmt"
)

func main() {
	var N, ans, cal int
	var S string
	var cal2 byte
	fmt.Scan(&N, &S)
	cal2 = S[0]
	cal = 1
	for i := 1; i < N; i++ {
		//fmt.Println(cal, cal2, S[i])
		if cal2 == S[i] {
			cal++
			cal2 = S[i]
			if i == N-1 {
				ans += (cal - 1) * cal / 2
			}
		} else if cal != 1 {
			//fmt.Println("g")
			ans += (cal - 1) * cal / 2
			cal2 = S[i]
			cal = 1
		} else {
			cal2 = S[i]
			cal = 1
		}
	}
	fmt.Println(ans)
}
