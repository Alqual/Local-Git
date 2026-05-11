package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)
var buffer = make([]byte, 10000)

func NewInt() int {
	sc.Scan()
	i, _ := strconv.Atoi(sc.Text())
	return i
}

func ceil(a, b int) int {
	if a%b == 0 {
		return a / b
	} else {
		return a/b + 1
	}
}

func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

func main() {
	T := NewInt()
	for i := 0; i < T; i++ {
		Case := NewInt()
		str := strconv.Itoa(Case)
		var ints []int
		for _, v := range str {
			d, _ := strconv.Atoi(string(v))
			ints = append(ints, int(d))
		}
		var ch,dh int = 0
		for j:= len(ints)-1; j >= 0; j-- {
			if ints[j] <=1 {
				if ch == 0 {
				ch = 1
				} else {
					fmt.Println(4)
				}
			} else {
				if ch == 0 {
					dh = max(ceil(ints[j],3),dh)
			} else {

			}
		
	}
}
