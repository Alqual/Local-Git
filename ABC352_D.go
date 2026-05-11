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

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func max(x, y int) int {
	if x < y {
		return y
	}
	return x
}

func main() {
	sc.Buffer(buffer, 3000000)
	W := Newline()
	P := Newline()
	chk := make(map[int]int, W[0]-W[1]+1)
	chk2 := make(map[int]int, W[0]-W[1]+1)
	var cons int
	for i := 0; i < W[0]; i++ {
		for j := max(P[i]+1-W[1], 0); j < min(P[i], W[0]); j++ {
			fmt.Println(i, j, P[i], W[1], P[i]+1-W[1], W[0])
			if chk[j] == 0 {
				chk2[j] = i + 1
			}
			chk[j]++
			if chk[j] == W[1] {
				fmt.Println(i + 1 - chk2[j])
				cons++
				break
			}
		}
		if cons == 1 {
			break
		}
	}
}
