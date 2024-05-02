package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// stdio //////////////
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
	ret := sc.Text()
	res, _ := strconv.Atoi(ret)
	return res
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}
func max(x, y int) int {
	if x < y {
		return y
	}
	return x
}

func main() {
	N := NewInt()
	A := make([]int, N)
	B := make([]int, N)
	for i := 0; i < N; i++ {
		W := Newline()
		A[i], B[i] = W[0], W[1]
	}
	var ans int
	ans = A[0] + B[0]

	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			if i == j {

				ans = min(ans, A[i]+B[j])
			} else {
				ans = min(ans, max(A[i], B[j]))
			}
		}
	}
	fmt.Println(ans)
}
