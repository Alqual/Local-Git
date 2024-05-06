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
var buffer = make([]byte, 300000)

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

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	sc.Buffer(buffer, 300000)
	N := NewInt()
	T := Newline()
	sort.Ints(T)
	var oven1, oven2, i int
	i = N - 1
	for i >= 0 {
		if i == N-1 {
			if N >= 2 {
				oven1 += T[i]
				oven2 += T[i-1]
				i -= 2
				continue
			} else {
				oven1 += T[i]
				break
			}

		}
		if oven1 > oven2 {
			oven2 += T[i]
		} else {
			oven1 += T[i]
		}
		i--
	}
	fmt.Println(max(oven1, oven2))
}
