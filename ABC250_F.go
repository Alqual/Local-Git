package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)
var buffer = make([]byte, 300000)

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

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func abs64(x float64) float64 {
	if x < 0 {
		return -x
	}
	return x
}

func square(x1, y1, x2, y2, x3, y3 int) int {
	return 2 * abs((x2-x3)*(y1-y3)-(x1-x3)*(y2-y3))
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	sc.Buffer(buffer, 3000000)
	N := NewInt()
	X := make([]int, N)
	Y := make([]int, N)
	chk := make([][]bool, N)
	var a0 int
	var a, c, b, s float64
	for i := 0; i < N; i++ {
		tmp := Newline()
		X[i] = tmp[0]
		Y[i] = tmp[1]
		if i > 1 {
			a0 += square(X[0], Y[0], X[i-1], Y[i-1], X[i], Y[i])
		}
		chk[i] = make([]bool, N)
	}
	a = float64(a0) / 4.0
	b = float64(square(X[0], Y[0], X[1], Y[1], X[2], Y[2]))
	for j := 0; j < N; j++ {
		c = 0
		for k := min(j+2, N-1); k < N; k++ {
			//fmt.Println(j, k, b, c, a0, a)
			if chk[j][k] || chk[k][j] {
				continue
			}
			c += float64(square(X[j], Y[j], X[k-1], Y[k-1], X[k], Y[k]))
			if abs64(c-a) > abs64(float64(a0)-c-a) {
				s = float64(a0) - c
			} else {
				s = c
			}
			if abs64(b-a) > abs64(s-a) {
				b = s
			}
			chk[j][k] = true
			chk[k][j] = true
		}
	}
	fmt.Println(int(2 * abs64(a-b)))

}
