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

func main() {
	sc.Buffer(buffer, 3000000)
	W := Newline()
	A := Newline()
	var res []int
	var ans int
	for i := 0; i < W[1]; i++ {
		if i == W[1]-1 {
			res = append(res, W[0]+A[0]-A[i])
		} else {
			res = append(res, A[i+1]-A[i])
		}
		if i == 0 {
			ans = res[i]
		} else if ans < res[i] {
			ans = res[i]
		}
		//fmt.Println(res)
	}
	fmt.Println(W[0] - ans)
}
