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
	A := make([]int, N)
	C := make([]int, N)
	for i := 0; i < N; i++ {
		W := Newline()
		A[i] = W[0]
		C[i] = W[1]
	}
	var maps map[int]int = map[int]int{}
	for i := 0; i < N; i++ {
		maps[A[i]] = i
	}
	sort.Ints(A)
	var chk []int = []int{}
	var ch int = 0
	chk = append(chk, A[N-1])
	for i := N - 2; i >= 0; i-- {
		if ch == 0 {
			if C[maps[A[i+1]]] >= C[maps[A[i]]] {
				chk = append(chk, A[i])
			} else {
				ch = A[i+1]
			}

		} else {
			if C[maps[ch]] >= C[maps[A[i]]] {
				chk = append(chk, A[i])
				ch = A[i]
			}
		}
	}
	var sorts []int = []int{}
	for i := 0; i < len(chk); i++ {
		sorts = append(sorts, maps[chk[i]]+1)
	}
	sort.Ints(sorts)
	fmt.Println(len(sorts))
	for i := 0; i < len(sorts); i++ {
		fmt.Print(sorts[i], " ")
	}
}
