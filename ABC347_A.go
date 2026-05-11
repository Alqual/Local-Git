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

func main() {
	W := Newline()
	A := Newline()
	var ans []int
	for i := 0; i < W[0]; i++ {
		if A[i]%W[1] == 0 {
			ans = append(ans, A[i]/W[1])
		}
	}
	for _, v := range ans {
		fmt.Println(v, "\n")
	}
}
