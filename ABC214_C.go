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

func dikstra(s int, d, V []int, prev []bool, S []int) {
	var Q []int = []int{}
	for i := 0; i < len(V); i++ {
		Q = append(Q, V[i])
	}
	for len(Q) > 0 {
		u := Q[0]
		Q = Q[1:]
		for i := 0; i < len(S[u]); i++ {
			v := S[u][i]
			if d[v] > d[u]+1 {
				d[v] = d[u] + 1
				prev[v] = true
				Q = append(Q, v)
			}
		}
	}
}

func main() {
	N := NewInt()
	S := Newline()
	T := Newline()
	var mins, mins2 int
	d := make([]int, N)
	prev := make([]bool, N)
	length := make([]int, N)
	V := make([]int, N)
	for i := 0; i < N; i++ {
		if i == 0 {
			mins = T[0]
			mins2 = 1
			V[0] = 1
		} else if T[i] < mins {
			mins = T[i]
			mins2 = i + 1
		}
		if i == 1 {
			length[i] = S[0]
			V[1] = 2
		} else if i >= 2 {
			length[i] = length[i-1] + S[i-1]
			V[i] = i + 1
		}
		if i == N-1 {
			V[i] = 0
		}
	}
	for i := 0; i < N; i++ {
		if i == mins2-1 {
			d[i] = 0
		} else {
			d[i] = 999999999
		}
	}

	fmt.Println(d, prev, S)

	//fmt.Println(L, T, N, S)
}
