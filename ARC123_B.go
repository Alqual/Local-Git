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
	s := strings.Fields(sc.Text())
	n := make([]int, len(s))
	for i, v := range s {
		n[i], _ = strconv.Atoi(v)
	}
	return n

}

func NewInt() int {
	sc.Scan()
	i, _ := strconv.Atoi(sc.Text())
	return i
}

func main() {
	sc.Buffer(buffer, 3000000)
	N := NewInt()
	A := Newline()
	B := Newline()
	C := Newline()
	sort.Ints(A)
	sort.Ints(B)
	sort.Ints(C)
	var ans, i, j, k int
	i = 0
	j = 0
	k = 0
	//fmt.Println(A, B, C)
	for i < N && j < N && k < N {
		//fmt.Println(i, j, k)
		for i < N && j < N && A[i] >= B[j] {
			j++
		}
		for j < N && k < N && B[j] >= C[k] {
			k++
		}
		if i < N && j < N && k < N && A[i] < B[j] && B[j] < C[k] {
			ans++
			i++
			j++
			k++
		}
	}
	fmt.Println(ans)
}
