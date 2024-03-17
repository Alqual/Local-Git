package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

const c = 50

var sc = bufio.NewScanner(os.Stdin)
var buffer = make([]byte, 10000)

func NewStrlines() []string {
	sc.Scan()
	return strings.Split(sc.Text(), " ")
}

func NewInt() int {
	sc.Scan()
	ret, _ := strconv.Atoi(sc.Text())
	return ret
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y

}

func main() {
	var n int
	fmt.Scan(&n)
	S := make([]string, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&S[i])
	}
	//var dp map[string]int = map[string]int{}
	var Lmin, xmin, cs int
	Lmin = len(S[0])
	xmin = 0
	var ans string
	for j := 1; j < n; j++ {
		Lmin = min(Lmin, len(S[j]))
		if len(S[j]) == Lmin {
			xmin = j
		}
	}
	ret := strings.Split(S[xmin], "")
	sort.Slice(ret, func(i, j int) bool {
		return ret[i] < ret[j]
	})
	for i := 0; i < Lmin; i++ {
		for j := 0; j < n; j++ {
			if strings.Contains(S[j], ret[i]) {
				cs++
			}
		}
		if cs == n {
			ans += ret[i]
			for k := 0; k < n; k++ {
				S[k] = strings.Replace(S[k], ret[i], "", 1)
			}
		}
		cs = 0
	}
	fmt.Println(ans)
}
