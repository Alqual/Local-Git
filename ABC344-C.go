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
	sc.Buffer(buffer, 3000000)
	N := NewInt()
	A := Newline()
	M := NewInt()
	B := Newline()
	L := NewInt()
	C := Newline()
	Q := NewInt()
	X := Newline()

	var dp map[int]bool = map[int]bool{}
	for i := 0; i < N; i++ {
		for j := 0; j < M; j++ {
			for k := 0; k < L; k++ {
				dp[A[i]+B[j]+C[k]] = true
			}
		}
	}
	for i := 0; i < Q; i++ {
		if dp[X[i]] == true {
			fmt.Println("Yes")
		} else {
			fmt.Println("No")
		}
	}
}
