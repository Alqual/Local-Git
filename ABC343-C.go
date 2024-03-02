package main

import (
	"fmt"
	"strconv"
)

const x = 1000000

func main() {
	var N int
	fmt.Scan(&N)
	var ans int
	for i := int(1); i <= x; i++ {
		if i*i*i <= N {
			T := strconv.Itoa(i * i * i)
			L := len(T)
			k := 0

			if L >= 2 {
				for j := 0; j < L/2; j++ {
					if string(T[j]) != string(T[L-1-j]) {
						k = 0
						break
					} else {
						k = 1
					}
				}
			} else {
				k = 1
			}

			if k == 1 && ans == 0 {
				ans = i * i * i
			} else if k == 1 && ans < i*i*i {
				ans = i * i * i
			}
		} else {
			break
		}
	}
	fmt.Println(ans)
}
