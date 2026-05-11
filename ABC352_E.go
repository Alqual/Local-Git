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

func main() {
	L := Newline()
	K := make([]int, L[1])
	C := make([]int, L[1])
	var A [][]int = [][]int{}
	for i := 0; i < L[1]; i++ {
		K[i] = Newline()[0]
		C[i] = Newline()[1]
		P := Newline()
		for j := 0; j < K[i]; j++ {
			A[i] = append(A[i], P[j]-1)
		}
	}
	ord := make([]int, L[1])
	for i := 0; i < L[1]; i++ {
		ord[i] = i + 1
	}
	sort.Slice(ord, func(i, j int) bool {
		return C[ord[i]] < C[ord[j]]
	})

}
