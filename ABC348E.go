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

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

type Graph map[int][]int

var ans Graph

func (g Graph) dfs(node int, visited map[int]bool, start, distance int, distances map[int]int, C []int) {
	visited[node] = true
	for _, next := range g[node] {
		if !visited[next] {
			g.dfs(next, visited, start, distance+1, distances, C)
		}
	}
}

func main() {
	sc.Buffer(buffer, 3000000)
	N := NewInt()
	G := make(Graph, N-1)
	C := make([]int, N)
	visited := make(map[int]bool)
	for i := 0; i < N; i++ {
		if i < N-1 {
			D := Newline()
			G[D[0]] = append(G[D[0]], D[1])
		} else {
			C = Newline()
		}
	}
	start := 1
	distances := make(map[int]int)
	G.dfs(start, visited, start, 0, distances, C)

}
