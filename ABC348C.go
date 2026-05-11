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

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	sc.Buffer(buffer, 3000000)
	N := NewInt()
	var cul map[int]int = map[int]int{}
	var ans int
	for i := 1; i <= N; i++ {
		D := Newline()
		if cul[D[1]] == 0 {
			cul[D[1]] = D[0]
		} else {
			cul[D[1]] = min(cul[D[1]], D[0])
		}
	}
	for i := range cul {
		if ans == 0 {
			ans = cul[i]
		} else if ans < cul[i] {
			ans = cul[i]
		}
	}
	fmt.Println(ans)
}
