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
	W := Newline()
	T := Newline()
	ar := make([]int, W[0])
	for i := 0; i < W[0]; i++ {
		ar[i] = 1
	}
	for i := 0; i < W[1]; i++ {
		if ar[T[i]-1] == 1 {
			ar[T[i]-1] = 0
		} else {
			ar[T[i]-1] = 1
		}
	}
	var ans int
	for i := 0; i < W[0]; i++ {
		ans += ar[i]
	}

	fmt.Println(ans)
}
