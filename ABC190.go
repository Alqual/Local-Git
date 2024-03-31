package main

import (
	"bufio"
	"os"
	"strconv"

	"golang.org/x/exp/maps"
)

var sc = bufio.NewScanner(os.Stdin)

func Newline() []int {
	var ret []int
	sc.Scan()
	for _, v := range sc.Text() {
		ar, _ := strconv.Atoi(v)
		ret = append(ret, ar)
	}
	return ret
}

func NewInt() int {
	sc.Scan()
	ret, _ := strconv.Atoi(sc.Text())
	return ret
}

func main() {
	W := Newline()
	var route map[int][]int = map[int][]int{}
	for i := 0; i < W[1]; i++ {
		D := Newline()
		route[D[0]] = append(route[D[0]], D[1])
		route[D[1]] = append(route[D[1]], D[0])
	}
	K := NewInt()
	C := Newline()
	keys := maps.Keys(route)

}
