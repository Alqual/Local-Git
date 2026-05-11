package main

import (
	"bufio"
	"fmt"
	"os"
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

func NewInt() int {
	sc.Scan()
	ret := sc.Text()
	res, _ := strconv.Atoi(ret)
	return res
}

func main() {
	sc.Buffer(buffer, 3000000)
	N := NewInt()
	A := Newline()
	var maps map[int]int = map[int]int{}
	var key []int
	for i := 0; i < N; i++ {
		if maps[A[i]] == 0 {
			key = append(key, A[i])
		}
		maps[A[i]]++
	}
	var ans int
	for i := 0; i < len(key); i++ {
		for j := 0; j < len(key); j++ {
			ans += maps[key[i]] * maps[key[j]] * (key[i] - key[j]) * (key[i] - key[j])
		}
	}
	fmt.Println(ans / 2)
}
