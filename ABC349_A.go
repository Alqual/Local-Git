package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)

func Newline() []int {
	sc.Scan()
	s := strings.Split(sc.Text(), " ")
	var ret []int
	for i := range s {
		num, _ := strconv.Atoi(s[i])
		ret = append(ret, num)
	}
	return ret
}

func NewInt() int {
	sc.Scan()
	i, _ := strconv.Atoi(sc.Text())
	return i
}

func main() {
	N := NewInt()
	A := Newline()
	var ans int
	//fmt.Println(A, N)
	for i := 0; i < N-1; i++ {
		ans += A[i]
	}
	fmt.Println(-1 * ans)
}
