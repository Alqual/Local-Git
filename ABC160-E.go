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

func NewInt() int {
	sc.Scan()
	ret, _ := strconv.Atoi(sc.Text())
	return ret
}

func Newline() []int {
	sc.Scan()
	arr := strings.Split(sc.Text(), " ")
	ret := make([]int, len(arr))
	for i, v := range arr {
		ret[i], _ = strconv.Atoi(v)
	}
	return ret
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {

	sc.Buffer(buffer, 3000000)
	W := Newline()
	P := Newline()
	Q := Newline()
	R := Newline()
	sort.Sort(sort.Reverse(sort.IntSlice(P)))
	sort.Sort(sort.Reverse(sort.IntSlice(Q)))
	sort.Sort(sort.Reverse(sort.IntSlice(R)))
	var cul, culA, culB, ans int
	for i := 0; i < W[0]; i++ {
		ans += P[i]
	}
	for i := 0; i < W[1]; i++ {
		ans += Q[i]
	}
	for (W[4] > cul) && (W[0] > culA) && (W[1] > culB) {
		mi := min(P[W[0]-1-culA], Q[W[1]-1-culB])
		if mi < R[cul] {
			ans += R[cul] - mi
			cul++
			if P[W[0]-1-culA] < Q[W[1]-1-culB] {
				culA++
			} else {
				culB++
			}
		} else {
			cul++
		}
	}
	fmt.Println(ans)

}
