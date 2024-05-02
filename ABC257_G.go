package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

type Pair struct {
	A, B int
}


var sc = bufio.NewScanner(os.Stdin)
var buffer = make([]byte, 300000)

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
	var A, B, C map[int][]int = map[int][]int{}, map[int][]int{}, map[int][]int{}
	var Pairs map[Pair]Pair = map[Pair]Pair{}
	for i := 0; i < N; i++ {
		D := Newline()
		if len(A[D[0]])!=0 || len(B[[1]]) !=0{
			Pairs[Pair{A: D[0], B: D[1]}] = Pair{A: D[0], B: D[1]}
		}
		A[D[0]] = append(A[D[0]], i + 1)
		B[D[1]] = append(B[D[1]], i + 1)
		C[D[2]] = append(C[D[2]], i + 1)
	}
}
