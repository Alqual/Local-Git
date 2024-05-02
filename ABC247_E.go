package main

import (
	"bufio"
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

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	sc.Buffer(buffer, 300000)
	W := Newline()
	A := Newline()
	var out []int
	var mins, maxs, count int
	for i := 0; i < W[0]; i++ {
		if W[1] > A[i] || W[2] < A[i] {
			out = append(out, W[i])
			i++
		}
	}
	for i := 1; i < len(out); i++ {
		var j int = out[i] + 1
		var k int = out[i] + 1

		for j <= out[i+1]-1 && k <= out[i+1]-1 {
			if A[k] == W[1] {
				mins++
			}
			if A[k] == W[2] {
				maxs++
			}
			if mins*maxs > 0 {
				count += out[i+1] - 1 - k
				if A[j] == W[1] {
					mins--
				}
				if A[j] == W[2] {
					maxs--
				}
				j++
			} else {
				k++
			}
		}
	}
}
