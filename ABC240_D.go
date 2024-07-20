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

func main() {
	N := NewInt()
	a := Newline()
	var cnt int
	var suc map[int]int = map[int]int{}
	var sli []int = []int{}
	for i := 0; i < N; i++ {
		if i == 0 {
			cnt++
			suc[a[i]]++
			sli = append(sli, a[i])
		} else if a[i] == a[i-1] {
			//fmt.Println("c", suc[a[i]])
			cnt++
			suc[a[i]]++
			if suc[a[i]] == a[i] {
				//	fmt.Println("e")
				cnt -= suc[a[i]]
				suc[a[i]] = 0
			}
		} else {
			//fmt.Println("d")
			cnt++
			suc[a[i]]++
			suc[a[i-1]] = 0
		}
		fmt.Println(cnt)
	}
}
