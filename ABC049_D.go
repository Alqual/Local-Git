package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

// search https://drken1215.hatenablog.com/entry/2021/07/28/014400
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

func dfs(g map[int][]int, v int, visit map[int]bool) {
	visit[v] = true
	for _, next_v := range g[v] {
		if visit[next_v] {
			continue
		}
		dfs(g, next_v, visit)
	}
}

func connected_components(g map[int][]int) map[int][]int {
	visited := map[int]bool{}
	visited2 := map[int]bool{}
	keys := map[int][]int{}
	for v := range g {
		if visited[v] {
			continue
		}
		dfs(g, v, visited2)
		for k := range visited2 {
			if !visited[k] {
				keys[len(visited2)-len(visited)-1] = append(keys[len(visited2)-len(visited)-1], k)
				visited[k] = true
			}
		}
		visited2 = visited
	}
	return keys
}

func main() {
	W := Newline()
	var Load map[int]int = map[int]int{}
	var Train map[int]int = map[int]int{}
	for i := 0; i < W[1]; i++ {
		X := Newline()
		Load[X[0]] = X[1]
		Load[X[1]] = X[0]
	}
	for i := 0; i < W[2]; i++ {
		Y := Newline()
		Train[Y[0]] = Y[1]
		Train[Y[1]] = Y[0]
	}

}
