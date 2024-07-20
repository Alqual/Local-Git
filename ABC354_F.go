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
	T := NewInt()
	for i := 0; i < T; i++ {
		N := NewInt()
		A := Newline()
		var dp int
		var maps map[int]int = map[int]int{}
		var maps2 []int = []int{}
		for i := 0; i < N; i++ {
			maps[A[i]] = i
		}
		sort.Ints(A)
		fmt.Println(A)
		var chk int
		dp = maps[A[0]]
		maps2 = append(maps2, maps[A[0]]+1)
		chk = 1
		for i := 1; i < N; i++ {
			fmt.Println(dp, maps[A[i]])
			if dp < maps[A[i]] {
				dp = maps[A[i]]
				chk++
				maps2 = append(maps2, maps[A[i]]+1)
			}
		}
		sort.Ints(maps2)
		fmt.Println(len(maps2))
		for i := 0; i < len(maps2); i++ {
			fmt.Print(maps2[i], " ")
		}
	}
}
