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

type Node struct {
	n     int
	Child []*Node
}

type Tree struct {
	Root *Node
}

func bfs(root *Node, C []int) map[int][]int {
	dist := make(map[int]int)     // 各ノードの距離を保存するマップ
	dist2 := make(map[int][]int)  // 各距離に対するノードを保存するマップ
	visited := make(map[int]bool) // 訪問済みノードを追跡するマップ
	queue := []*Node{root}        // 処理対象のノードを格納するキュー
	sums := make([]int, len(C))

	dist[root.n] = 0                    // ルートノードの距離は0
	dist2[0] = append(dist2[0], root.n) // 距離0に対するルートノードを設定

	for len(queue) > 0 {
		current := queue[0] // キューからノードを取り出す
		queue = queue[1:]
		// 現在のノードの子ノードを探索
		for _, child := range current.Child {
			if !visited[child.n] {
				visited[child.n] = true // 子ノードを訪問済みとマーク
				p1 := dist[current.n]
				dist[child.n] = p1 + 1 // 子ノードの距離を設定
				dist2[p1+1] = append(dist2[p1+1], child.n)
				queue = append(queue, child) // キューに子ノードを追加
				fmt.Println(current.n+1, child.n+1, dist[child.n], C[current.n], sums[current.n])
			}
		}
	}
	return dist2
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func main() {
	sc.Buffer(buffer, 3000000)
	N := NewInt()
	nodes := make([]*Node, N)
	for i := 0; i < N; i++ {
		nodes[i] = &Node{n: i}
	}
	C := make([]int, N)
	for i := 0; i < N; i++ {
		if i < N-1 {
			D := Newline()
			parent := D[0] - 1
			child := D[1] - 1
			nodes[parent].Child = append(nodes[parent].Child, nodes[child])
			nodes[child].Child = append(nodes[child].Child, nodes[parent])
		} else {
			C = Newline()
		}
	}
	var dist map[int][]int = map[int][]int{}
	dist = bfs(nodes[0], C)
	var keys []int
	for k := range dist {
		keys = append(keys, k)
	}
	keys_med := keys[len(keys)/2]
	var ans int
	for i := range keys {
		for j := range dist[i] {
			ans += (abs(dist[i][j] - keys_med)) * C[j]
		}
	}
	fmt.Println(ans)
}
