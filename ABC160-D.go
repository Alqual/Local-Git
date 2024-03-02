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
	arr := strings.Split(sc.Text(), " ")
	ret := make([]int, len(arr))
	for i, v := range arr {
		ret[i], _ = strconv.Atoi(v)
	}
	return ret
}

type key struct {
	x int
	y int
}

func main() {
	sc.Buffer(buffer, 3000000)
	W := Newline()
	W[1]--
	W[2]--
	var dist map[key]int = map[key]int{}
	//fmt.Println(dist)
	for i := 0; i < W[0]; i++ {
		for j := 0; j < W[0]; j++ {
			dist[key{i, j}] = -1
		}
	}
	for k := 0; k < W[0]; k++ {
		var queue []int
		queue = append(queue, k)
		dist[key{k, k}] = 0
		for len(queue) > 0 {
			v := queue[0]
			queue = queue[1:]
			var nvs []int
			if v > 0 {
				nvs = append(nvs, v-1)
			}
			if v < W[0]-1 {
				nvs = append(nvs, v+1)
			}
			if v == W[1] {
				nvs = append(nvs, W[2])
			}
			if v == W[2] {
				nvs = append(nvs, W[1])
			}
			for _, nv := range nvs {
				if dist[key{k, nv}] == -1 {
					dist[key{k, nv}] = dist[key{k, v}] + 1
					queue = append(queue, nv)
				}
			}
		}
	}
	var res []int = make([]int, W[0])
	for i := 0; i < W[0]; i++ {
		for j := i + 1; j < W[0]; j++ {
			res[dist[key{i, j}]]++
		}
	}
	for k := 1; k < W[0]; k++ {
		fmt.Println(res[k])
	}
}
