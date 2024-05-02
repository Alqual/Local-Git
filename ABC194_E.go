package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

// stdio //////////////
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
func max(x, y int) int {
	if x < y {
		return y
	}
	return x
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func main() {
	sc.Buffer(buffer, 3000000)
	W := Newline()
	var maps map[int][]int
	var ans, ans2 int
	for i:= 1; i<= W[0]; i++{
		A := Newline()
		maps[A[0]] = append(maps[A[0]],i)
	}
	