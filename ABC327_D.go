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

func dfs(graph map[int][]int, node int, c int, color map[int]int) bool {
	color[node] = c
	for _, next := range graph[node] {
		if color[next] == 0 {
			if !dfs(graph, next, -c, color) {
				return false
			}
		} else if color[next] != -c {
			return false
		}
	}
	return true
}

func bintree(graph map[int][]int) bool {
	var n int = len(graph)
	color := make(map[int]int, n)
	for i := 1; i <= n; i++ {
		if color[i] != 0 {
			continue
		}
		if !dfs(graph, i, 1, color) {
			return false
		}
	}
	return true
}

func bfs(graph map[int][]int, node int, visited map[int]bool, check map[int]int) string {
	visited[node] = true
	queue := []int{}
	for keys := range graph {
		queue = append(queue, keys)
	}
	check[queue[0]] = 1
	for len(queue) > 0 {
		node = queue[0]
		queue = queue[1:]
		for _, next := range graph[node] {
			if !visited[next] {
				visited[next] = true
				if check[node] == 1 {
					check[next] = -1
				} else {
					check[next] = 1
				}
				queue = append(queue, next)
			} else if check[node] == check[next] {
				return "No"
			}
		}
	}
	return "Yes"
}

func main() {
	sc.Buffer(buffer, 3000000)
	W := Newline()
	A := Newline()
	B := Newline()
	var maps map[int][]int = map[int][]int{}
	var test bool
	for i := 0; i < W[1]; i++ {
		maps[A[i]] = append(maps[A[i]], B[i])
		maps[B[i]] = append(maps[B[i]], A[i])
	}
	test = bintree(maps)
	if test {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
