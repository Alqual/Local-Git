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

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func main() {
	sc.Buffer(buffer, 3000000)
	W := Newline()
	X := Newline()
	Y := Newline()
	dpx := make(map[int]int, W[0]-1)
	dpy := make(map[int]int, W[1]-1)
	dpx[0] = (X[1] - X[0]) * (Y[1] - Y[0])
	for i := 2; i < W[0]; i++ {
		dpx[i] += dpx[x-1] + (dpx[i-1] - dpx[i-2]) + (X[i]-X[i-1])*(Y[1]-Y[0])
	}
	dpy[0] = dpx[W[0]-1]
	for i := 2; i < W[1]; i++ {
		dpy[i] += dpy[i-1] + (dpy[i-1] - dpy[i-2]) + (X[W[0]-1]-X[0])*(Y[i]-Y[i-1])
	}
	fmt.Println(dpy[W[1]-1])
}
