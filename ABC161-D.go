package main

//単純計算ではどの様にやっても間に合わない

import (
	"fmt"
	"strconv"
)

const v = 1000000000
const u = "0000000000"

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	var K int
	fmt.Scan(&K)
	var ans, c, c2 int

	for i := 1; i <= 99; i++ {
		d := strconv.Itoa(i)
		if len(d) == 1 {
			c++
		} else if len(d) == 2 {
			s, _ := strconv.Atoi(string(d[0]))
			t, _ := strconv.Atoi(string(d[1]))
			if abs(s-t) <= 1 {
				c++
			}
		}
		if c == K {
			ans = i
			break
		}
	}
	if ans == 0 {
		for i := 100; i <= v; i++ {
			//fmt.Println(i)
			d := fmt.Sprint(i)
			for j := 0; j < len(d)-1; j++ {
				if abs(int(d[j])-int(d[j+1])) <= 1 {
					c2 = 1
				} else {
					if (j == 0) && (int(d[0]) < 9) {
						d = string(int(d[0])+1) + string(int(d[0])) + u[:len(d)-2]
						j, _ := strconv.Atoi(d)
						i = j
					}
					c2 = 0
					break
				}
			}
			if c2 == 1 {
				c++
			}
			c2 = 0
			if c == K {
				ans = i
				break
			}
		}
	}
	fmt.Println(ans)
}
