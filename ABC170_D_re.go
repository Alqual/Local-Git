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
	var chk map[int]bool = map[int]bool{}
	var ans int
	for i := 0; i < N; i++ {
		for j := 0; j < N; j++ {
			if i == j || chk[A[j]] {
				continue
			}
			if A[i] == A[j] || A[j]%A[i] == 0 {
				chk[A[j]] = true
			}
		}
	}
	for i := 0; i < N; i++ {
		if !chk[A[i]] {
			ans++
		}
	}
	fmt.Println(ans)
}
