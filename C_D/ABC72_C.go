package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)
var buffer = make([]byte, 10000)

func Newline() []int {
	sc.Scan()
	arr := strings.Split(sc.Text(), " ")
	ret := make([]int, len(arr))
	for i, v := range arr {
		ret[i], _ = strconv.Atoi(v)
	}
	return ret
}

func NewInt() int {
	sc.Scan()
	ret, _ := strconv.Atoi(sc.Text())
	return ret
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	sc.Buffer(buffer, 3000000)
	N := NewInt()
	a := Newline()
	var ans, ans2 int
	var cons []int
	var cul map[int]int = map[int]int{}

	for i := 0; i < N; i++ {
		cul[a[i]]++
	}
	for v, _ := range cul {
		cons = append(cons, v)
	}
	sort.Ints(cons)
	for i := 0; i < len(cons); i++ {

		if len(cons) == 1 {
			ans = cul[cons[0]]
			break
		}

		if len(cons) == 2 {
			if abs(cons[0]-cons[1]) <= 1 {
				ans = cul[cons[0]] + cul[cons[1]]
			} else {
				ans = max(cul[cons[0]], cul[cons[1]])
			}
			break
		}

		if i >= 2 {
			if abs(cons[i]-cons[i-1]) <= 1 {
				if ans2 == 0 {
					ans2 = cul[cons[i]] + cul[cons[i-1]]
				} else if ans2 < cul[cons[i]]+cul[cons[i-1]] {
					ans2 = cul[cons[i]] + cul[cons[i-1]]
				}
				if abs(cons[i]-cons[i-1]) <= 1 && abs(cons[i-1]-cons[i-2]) <= 1 {
					if ans == 0 {
						ans = cul[cons[i]] + cul[cons[i-1]] + cul[cons[i-2]]
					} else if ans < cul[cons[i]]+cul[cons[i-1]]+cul[cons[i-2]] {
						ans = cul[cons[i]] + cul[cons[i-1]] + cul[cons[i-2]]
					}
				}
			}

			//fmt.Println(cul, i, cons, ans)

		}
	}
	if ans == 0 {
		fmt.Println(ans2)
	} else {
		fmt.Println(ans)
	}
}
