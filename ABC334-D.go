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
	W := Newline()
	R := Newline()
	Soli := make([]int, W[0])
	Shika := make([]int, W[1])
	Shika0 := make([]int, W[1])
	ans := make(map[int]int, W[1])
	sort.Ints(R)
	Soli[0] = R[0]
	for i := 1; i < W[0]; i++ {
		Soli[i] += Soli[i-1] + R[i]
	}
	for j := 0; j < W[1]; j++ {
		Q := NewInt()
		Shika[j] = Q
		Shika0[j] = Q
	}
	sort.Ints(Shika)
	var i, j int = 0, 0
	for i < W[0] && j < W[1] {
		//fmt.Println(i, j, Soli[i], Shika[j])
		if Shika[j] >= Soli[i] {
			i++
			if i == W[0] {
				ans[Shika[j]] = W[0]
				if j < W[1] {
					for j < W[1] {
						ans[Shika[j]] = W[0]
						j++
					}
				}
			}
		} else {
			ans[Shika[j]] = i
			j++
		}
	}
	//fmt.Println(ans)
	for _, v := range Shika0 {
		fmt.Println(ans[v])
	}
}
