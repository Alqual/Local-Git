package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const c = 998244353

var sc = bufio.NewScanner(os.Stdin)
var buffer = make([]byte, 10000)

func Newline() []int {
	sc.Scan()
	s := strings.Fields(sc.Text())
	n := make([]int, len(s))
	for i, v := range s {
		n[i], _ = strconv.Atoi(v)
	}
	return n
}

func Newstrline() []string {
	sc.Scan()
	s := strings.Fields(sc.Text())
	return s
}

func main() {
	W := Newline()
	C := make([]string, W[1])
	K := make([]int, W[1])
	for i := 0; i < W[1]; i++ {
		Z := Newstrline()
		C[i] = Z[0]
		K[i], _ = strconv.Atoi(Z[1])
	}
	var ans, cin int
	for i := 1; i <= W[0]; i++ {
		for j := 0; j < W[1]; j++ {
			if C[j] == "R" && K[j] > i {
				cin++
			} else if C[j] == "L" && K[j] < i {
				cin++
			}
			if K[j] == i {
				cin = 1
				break
			}
		}
		if cin > 0 {
			if ans == 0 {
				ans = cin
			} else {
				ans *= cin
				ans %= c
			}
		}
		cin = 0
	}
	fmt.Println(ans)
}
