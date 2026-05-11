package main

import (
	"bufio"
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
	Z := Newline()
	A := make([]string, Z[0])
	var stH, stW, goH, goW int
	for i := 0; i < Z[0]; i++ {
		sc.Scan()
		A[i] = sc.Text()
		if strings.Contains(A[i], "S") {
			stH = i + 1
			stW = strings.Index(A[i], "S")
		}
		if strings.Contains(A[i], "T") {
			goH = i + 1
			goW = strings.Index(A[i], "T")
		}
	}
	N := NewInt()
	var B [][]int = [][]int{}
	for i := 0; i < N; i++ {
		B = append(B, Newline())
	}
}
