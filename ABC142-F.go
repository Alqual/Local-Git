package main

import (
	"bufio"
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

func main() {
	sc.Buffer(buffer, 3000000)
	N := Newline()
	var Graph map[int][]int
	for i := 0; i < N[1]; i++ {
		ab := Newline()
		ab[0]--
		ab[1]--
		Graph[ab[0]] = append(Graph[ab[0]], ab[1])
	}
	var short int = N[0]+1
	var res []int
	dist := make([]int, N[0])
	prev := make([]int, N[0])
	

	for j := 0; j < N[0]; i++ {


}
