package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const limit = 50

var sc = bufio.NewScanner(os.Stdin)
var tree map[Node]bool = map[Node]bool{}
var a, b = []int{}, []int{}
var visited = make([]bool, limit)
var W = make([]int, 2)

func nextLine() []int {
	sc.Scan()
	arr := strings.Split(sc.Text(), " ")
	ret := make([]int, len(arr))
	for i, v := range arr {
		ret[i], _ = strconv.Atoi(v)
	}
	return ret
}

func dfs(v int) {
	visited[v] = true
	n := W[0]
	for i := 0; i < n; i++ {
		if tree[Node{v, i}] == false {
			continue
		}
		if visited[i] == true {
			continue
		}
		dfs(i)
	}
}

type Node struct {
	Bef  int
	Next int
}

func main() {
	W = nextLine()
	var ans int = 0
	fmt.Println(tree)

	for i := 0; i < W[1]; i++ {
		ab := nextLine()
		ab[0]--
		ab[1]--
		tree[Node{ab[0], ab[1]}] = true
		tree[Node{ab[1], ab[0]}] = true
		a = append(a, ab[0])
		b = append(b, ab[1])
	}
	delete(tree, Node{0, 0})
	fmt.Println(tree)
	//fmt.Println(a, b)
	for i := 0; i < W[1]; i++ {
		tree[Node{a[i], b[i]}] = false
		tree[Node{b[i], a[i]}] = false
		for j := 0; j < W[0]; j++ {
			visited[j] = false
		}
		dfs(0)
		//fmt.Println(visited)
		var bridge bool = false
		for k := 0; k < W[0]; k++ {
			if visited[k] == false {
				fmt.Println("a")
				bridge = true
			}
			fmt.Println(bridge, visited[k])
		}
		if bridge == true {
			fmt.Print("bridge: ")
			ans++
		}
		tree[Node{a[i], b[i]}] = true
		tree[Node{b[i], a[i]}] = true
		fmt.Println(tree, a[i], b[i])
	}
	//tree[Node{}] = nil
	//fmt.Println(tree)
	fmt.Println(ans)
}
