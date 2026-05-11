package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const inf int = 1 << 29
const max_v int = 110
const max_e int = 1100

type key struct {
	x, y int
}

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

/////////////////////

// Floyd-warshall ///////////////

func FW(dist map[key]int, n int) map[key]int {
	for k := 0; k < n; k++ {
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				if dist[key{i, j}] > dist[key{i, k}]+dist[key{k, j}] {
					dist[key{i, j}] = dist[key{i, k}] + dist[key{k, j}]
				}
			}
		}
	}
	return dist
}

func sol(dist map[key]int, a, b, c []int) int {
	var res int
	for i := 0; i < len(c); i++ {
		if dist[key{a[i], b[i]}] < c[i] {
			res++
		}
	}
	return res
}

func main() {
	W := Newline()
	a := make([]int, W[1])
	b := make([]int, W[1])
	c := make([]int, W[1])
	dist := make(map[key]int, W[0]*W[0])
	for i := 0; i < W[0]; i++ {
		for j := 0; j < W[0]; j++ {
			if i == j {
				dist[key{i, j}] = 0
			} else {
				dist[key{i, j}] = inf
			}
		}
	}
	for i := 0; i < W[1]; i++ {
		T := Newline()
		a[i], b[i], c[i] = T[0]-1, T[1]-1, T[2]
		dist[key{a[i], b[i]}] = c[i]
		dist[key{b[i], a[i]}] = c[i]
	}
	dist = FW(dist, W[0])
	fmt.Println(sol(dist, a, b, c))
}
