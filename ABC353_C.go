package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

const c = 100000000

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
	sc.Buffer(buffer, 3000000)
	N := NewInt()
	A := NewLine()
	for i := 0; i < N; i++ {
		A[i] %= c
	}
	sort.Ints(A)
	chk := make([]int, N)
	var chk2 int
	for i := 0; i < N; i++ {
		for j := i + 1; j < N; j++ {
			if A[i]+A[j] >= c {
				chk[i] = N - j
				break
			}
		}
		if i < N-1 && A[i]+A[i+1] >= c {
			chk2 = i
			break
		}
	}
	var ans int
	for i := 0; i < N; i++ {
		if i<chk2 {
		ans += A[i]*(N-1) - chk[i]*c
	} else {
		ans += A[i]*(N-1) - (N-i-1)*c
	}
	fmt.Println(ans)
}
