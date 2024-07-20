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

func NewLine() []int {
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

func main() {
	N := NewInt()
	H := NewLine()
	var a, b int = 0, 0
	for i := 1; i < N; i++ {
		if H[i] > H[0] {
			if a == 0 {
				a = H[i]
				b = i + 1
				break
			}
		}
	}
	if a == 0 {
		fmt.Println(-1)
	} else {
		fmt.Println(b)
	}
}
