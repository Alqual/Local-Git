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

func Newtext() []string {
	sc.Scan()
	ret := strings.Split(sc.Text(), " ")
	return ret
}

func main() {
	N := NewInt()
	S := make([]string, N)
	var rate int
	for i := 0; i < N; i++ {
		W := Newtext()
		S[i] = W[0]
		ret, _ := strconv.Atoi(W[1])
		rate += ret
	}
	sort.Slice(S, func(i, j int) bool {
		return S[i] < S[j]
	})
	win := rate % N
	fmt.Println(S[win])
}
