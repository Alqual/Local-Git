package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)
var buffer = make([]byte, 10000)

func NewLine() []int {
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

func main() {
	N := NewInt()
	A := NewLine()
	B := make(map[int]int, N)
	var key []int = []int{}
	for i := 0; i < N; i++ {
		B[A[i]] = i
	}
	for i := range B {
		key = append(key, i)
	}
	sort.Ints(key)
	sum := make([]int, N)
	C := make(map[int]int, N)
	sum[0] = key[0]
	C[key[0]] = 1
	for i := 1; i < N; i++ {
		sum[i] += sum[i-1] + key[i]
		C[key[i]] = i + 1

	}
}
