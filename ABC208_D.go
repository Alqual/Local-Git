package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const c = 1 << 60

// / stdin/out ///
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

//////

/// Calculation ///

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func WarshallFloyd(n int, maps [][]int) int {
	var ans int
	for k := 0; k < n; k++ {
		nxt := make([][]int, n)
		for i := 0; i < n; i++ {
			nxt[i] = make([]int, n)
		}
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				nxt[i][j] = min(maps[i][j], maps[i][k]+maps[k][j])
				if nxt[i][j] < 1<<59 {
					ans += nxt[i][j]
				}

			}
		}
		maps = nxt
	}
	return ans
}

func main() {
	W := Newline()
	maps := make([][]int, W[0])
	for i := 0; i < W[0]; i++ {
		maps[i] = make([]int, W[0])
	}
	for i := 0; i < W[1]; i++ {
		edge := Newline()
		maps[edge[0]-1][edge[1]-1] = edge[2]
	}
	for i := 0; i < W[0]; i++ {
		for j := 0; j < W[0]; j++ {
			if i != j && maps[i][j] == 0 {
				maps[i][j] = c
			}
		}
	}
	fmt.Println(WarshallFloyd(W[0], maps))
}
