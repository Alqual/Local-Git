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

func main() {
	sc.Buffer(buffer, 3000000)
	N := NewInt()
	A := Newline()
	var maps2 map[int]int = map[int]int{}
	var maps map[int]int = map[int]int{}
	var ar [][]int
	for ind, ar := range A {
		maps2[ind+1] = ar
		maps[ar] = ind + 1
	}
	for i := 1; i <= N; i++ {
		if len(ar) == N-1 {
			break
		}
		if maps2[i] == i {
			continue
		} else {
			if maps[i] > i {
				ar = append(ar, []int{i, maps[i]})
				//fmt.Println(i, maps2[i])
			} else {
				ar = append(ar, []int{maps[i], i})
				//fmt.Println(maps2[i], i)
			}
			v := maps[i]
			w := maps2[i]
			maps2[v] = w
			maps2[i] = i
			maps[w] = v
			maps[i] = i
			//d := maps[maps2[maps[i]]]
			//maps[i] = d
		}
	}
	fmt.Println(len(ar))
	for _, ar_ := range ar {
		fmt.Println(ar_[0], ar_[1])
	}
}
