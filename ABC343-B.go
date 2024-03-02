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
var buffer = make([]byte, 10000)

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

// 重複要素を削除する関数
func removeDuplicates(elements []int) []int {
	// 重複をチェックするためのマップ
	encountered := map[int]bool{}
	// 重複がない要素を保持するスライス
	result := []int{}

	for v := range elements {
		if encountered[elements[v]] == true {
			// 既に存在する場合は追加しない
		} else {
			// 重複がない場合は追加する
			encountered[elements[v]] = true
			result = append(result, elements[v])
		}
	}
	return result
}

func main() {
	sc.Buffer(buffer, 3000000)
	N := NewInt()
	var maps map[int][]int = map[int][]int{}
	for i := 0; i < N; i++ {
		K := Newline()
		for j := 0; j < N; j++ {
			if K[j] == 1 {
				maps[j+1] = append(maps[j+1], i+1)
				maps[i+1] = append(maps[i+1], j+1)
			}
		}
	}
	//fmt.Println(maps)
	for i := 0; i < N; i++ {
		Z := maps[i+1]
		sort.Ints(Z)
		V := removeDuplicates(Z)
		var W []string
		for j := range V {
			W = append(W, strconv.Itoa(V[j]))
		}
		fmt.Println(strings.Join(W, " "))
	}
}
