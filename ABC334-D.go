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
	sc.Buffer(buffer, 300000)
	W := Newline()
	R := Newline()
	Soli := make([]int, W[0])
	sort.Ints(R)
	Soli[0] = R[0]
	var ans []int
	for i := 1; i < W[0]; i++ {
		Soli[i] += Soli[i-1] + R[i]
	}
	Soli2 := make([]int, Soli[W[0]-1])
	c := 0
	for i := 1; i <= Soli[W[0]-1]; i++ {
		if Soli[c] <= i {
			c++
		}
		Soli2[i-1] += c
	}
	fmt.Println(Soli, Soli2)
	for i := 0; i < W[1]; i++ {
		Q := NewInt()
		if Q < Soli[W[0]-1] {
			ans = append(ans, Soli2[Q-1])
		} else {
			ans = append(ans, W[0])
		}
	}
	for _, a := range ans {
		fmt.Println(a)
	}
}
