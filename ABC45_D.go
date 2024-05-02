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

type key struct {
	x, y int
}

func main() {
	sc.Buffer(buffer, 300000)
	Z := Newline()
	var C map[key]bool = map[key]bool{}
	for i := 0; i < Z[2]; i++ {
		W := Newline()
		C[key{W[0], W[1]}] = true
	}

	ans := make([]int, 10)
	var cout, chk, chk2 int
	var visited map[key]bool = map[key]bool{}
	for keys := range C {
		for i := keys.x - 1; i <= keys.x+1; i++ {
			for j := keys.y - 1; j <= keys.y+1; j++ {
				if !visited[key{i, j}] {
					visited[key{i, j}] = true
				} else {
					continue
				}
				for k := i - 1; k <= i+1; k++ {
					for l := j - 1; l <= j+1; l++ {
						if C[key{k, l}] {
							cout++
						}
						if k >= 1 && k <= Z[0] && l >= 1 && l <= Z[1] {
							chk++
						}
					}
				}
				if chk == 9 {
					ans[cout]++
					chk2++
				}
				chk = 0
				cout = 0
			}
		}
	}
	ans[0] += (Z[0]-2)*(Z[1]-2) - chk2
	for i := 0; i < 10; i++ {
		fmt.Println(ans[i])
	}
}
