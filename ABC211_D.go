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
const c0 int = 1000000007

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

////  dfs /////////////////

func dfs(v, w int, g [][]int, cout, res, cn int, visited map[int]bool) int {
	visited[v] = true
	for _, next_v := range g[v] {
		if next_v == w {
			fmt.Println("a", cn, cout, res)
			if !visited[w] {
				fmt.Println("b")
				cn = cout
				res++
				res %= c0
				visited[w] = true
			} else if cn > cout {
				fmt.Println("c")
				cn = cout
				res = 1
			} else if cn == cout {
				fmt.Println("d")
				res++
				res %= c0

			}
			continue
		}
		if !visited[next_v] {
			dfs(next_v, w, g, cout+1, res, cn, visited)
		}
	}
	return res
}

func sol(n, m int, g [][]int) int {
	var res, cn, cout int = 0, 0, 0
	var visited map[int]bool = map[int]bool{}
	res = dfs(n, m, g, cout, res, cn, visited)
	fmt.Println(res)
	return res
}

func main() {
	W := Newline() //N M
	g := make([][]int, W[1]*W[1])
	for i := 0; i < W[1]; i++ {
		ab := Newline()
		g[ab[0]] = append(g[ab[0]], ab[1])
		g[ab[1]] = append(g[ab[1]], ab[0])
	}
	res := sol(1, W[0], g)
	fmt.Println(res)
}
