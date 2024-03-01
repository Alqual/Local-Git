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

func order(N int, X []int) int {
	var ans, l int
	var W []int
	var maps map[int]bool = map[int]bool{}
	for i := 0; i < N; i++ {
		W = append(W, i+1)
	}

	for ind, i := range X {
		d := 1
		maps[i] = true
		for k := range W {
			if maps[k] != true {
				l++
			}
			if k == i {
				break
			}
		}
		//fmt.Println(ind, i)
		for j := 1; j <= (N - ind - 1); j++ {
			d *= j
		}
		ans += (l - 1) * d
		if ind == N-1 {
			ans++
		}
		l = 0
	}

	return ans
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	sc.Buffer(buffer, 3000000)
	N := NewInt()
	P := Newline()
	Q := Newline()
	//fmt.Println(order(N, P), order(N, Q))
	fmt.Print(abs(order(N, P) - order(N, Q)))
}
