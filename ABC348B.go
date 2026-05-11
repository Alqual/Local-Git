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
	ret := strings.Split(sc.Text(), " ")
	var reti []int
	for _, s := range ret {
		res, _ := strconv.Atoi(s)
		reti = append(reti, res)
	}
	return reti
}

func NewInt() int {
	sc.Scan()
	ret, _ := strconv.Atoi(sc.Text())
	return ret
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	sc.Buffer(buffer, 3000000)
	N := NewInt()
	X := make([]int, N)
	Y := make([]int, N)
	var ans, d, c1 int
	for i := 0; i < N; i++ {
		Z := Newline()
		X[i] = Z[0]
		Y[i] = Z[1]
	}
	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			if j != i {
				d = (X[j]-X[i])*(X[j]-X[i]) + (Y[j]-Y[i])*(Y[j]-Y[i])
				if ans == 0 {
					ans = d
					c1 = j + 1
				} else if ans < d {
					ans = d
					c1 = j + 1
				}
			}
			if j == N-1 {
				fmt.Println(c1)
				ans = 0
				c1 = 0
			}
		}
	}
}
