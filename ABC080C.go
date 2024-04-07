package main

import (
	"bufio"
	"fmt"
	"os"
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

func main() {
	N := NewInt()
	var F, P [][]int = [][]int{}, [][]int{}
	var ans, co, min int = 0, 0, 0
	co2 := make([]int, N)
	for i := 0; i < N; i++ {
		F = append(F, Newline())
	}
	for i := 0; i < N; i++ {
		P = append(P, Newline())
	}
	fmt.Println(F, P, F[0][1])
	for i := 0; i < 10; i++ {
		if i == 0 {
			for j := 0; j < N; j++ {
				ans += P[0][j]
			}
		} else {
			d := 0
			for j := 0; j < N; j++ {
				if F[j][i] == 1 {
					d += P[j][i]
				}
			}
			if d > 0 && d> {
				ans += d
				co++
			} else {
				if min == 0 {
					min = d
				} else {
					if min < d {
						min = d
					}
				}
			}
			if co == 0 {
				ans += min
			}
		}
	}
	fmt.Println(ans)
}
