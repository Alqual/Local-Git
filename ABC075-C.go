package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)

func nextLine() []int {
	sc.Scan()
	arr := strings.Split(sc.Text(), " ")
	ret := make([]int, len(arr))
	for i, v := range arr {
		ret[i], _ = strconv.Atoi(v)
	}
	return ret
}

func dfs(v,n int, visited []bool, tree map[Node]bool) {
	visited[v] = true
	for i := 0; i < n; i++ {
		if tree[Node{v,i}] == false && visited[i] == true {
			dfs(i,n,visited,tree)
		}


	}
}


type Node struct {
	Bef  int
	Next int
}

func main() {
	W := nextLine()
	var tree map[Node]bool = map[Node]bool{}
	var a,b []int
	visited := make( []bool, W[0])

	for i := 0; i < W[1]; i++ {
		ab := nextLine()
		ab[0]--
		ab[1]--
		tree[Node{ab[0], ab[1]}] = true
		tree[Node{ab[1], ab[0]}] = true
		a = append(a, ab[0])
		b = append(b, ab[1])
	}
	fmt.Println(tree)

	for i := 0; i < W[1]; i++ {
		tree[Node{a[0], b[0]}] = false
		tree[Node{b[0], a[0]}] = false
		for j := 0; j < W[0]; j++ {
			visited[j] = false
			dfs(0)
			var bridge bool = false
			for k := 0; k < W[0]; k++ {
				if visited[k] == false {
					bridge = true
				}

			}
		}








	//tree[Node{}] = nil
	fmt.Println(tree)
}
