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
	A := make([]int, N)
	B := make([]int, N)
	var maxB, ans int
	for i := 0; i < N; i++ {
		Z := Newline()
		A[i] = Z[0]
		B[i] = Z[1]
		if i == 0 {
			maxB = B[i] - A[i]
		} else {
			if B[i]-A[i] > maxB {
				maxB = B[i] - A[i]
			}
		}
		ans += A[i]
	}
	fmt.Println(ans + maxB)
}
