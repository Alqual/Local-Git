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

func floor(x, y int) int {
	if float64(x/y) > float64(int(x/y)) {
		return x/y + 1
	}
	return x / y
}

func main() {
	sc.Buffer(buffer, 3000000)
	W := Newline()
	A := Newline()
	var sum int
	var maps []int
	for i := 0; i < W[0]; i++ {
		sum += A[i]
	}

	for i := 0; i < W[0]; i++ {
		if float64(A[i]) >= float64(sum)/float64(4*W[1]) {
			maps = append(maps, i)
		}
	}
	if len(maps) >= W[1] {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
