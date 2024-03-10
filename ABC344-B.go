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
	arr := strings.Split(sc.Text(), " ")
	ret := make([]int, len(arr))
	for i, v := range arr {
		ret[i], _ = strconv.Atoi(v)
	}
	return ret
}

func main() {
	var A []int = []int{}
	for {
		var A_ int
		fmt.Scan(&A_)
		if A_ != 0 {
			A = append(A, A_)
		} else {
			A = append(A, 0)
			break
		}
	}
	L := len(A)
	for i := 0; i < L; i++ {
		fmt.Println(A[L-1-i])

	}
}
