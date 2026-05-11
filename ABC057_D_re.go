package main

import (
	"bufio"
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

func main() {
	W := Newline() //N A B
	V := Newline() //v1 v2 ... vn
	var maps map[int]int
	for i := 0; i < W[0]; i++ {
		maps[V[i]]++
	}
	var keys []int
	for k := range maps {
		keys = append(keys, k)
	}
	sort.Ints(keys)
	var cns int = len(keys)
	var sum int
	for cns >= 0 {
		sum += keys[cns]
		if sum >= W[1] {
			break
		}
		cns--
	}

}
