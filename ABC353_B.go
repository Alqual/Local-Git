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

func NewLine() []int {
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
	W := NewLine()
	A := NewLine()
	var ans, cout int = 0, W[1]
	for i := 0; i < W[0]; i++ {
		//fmt.Println(ans, i, cout)
		if cout >= A[i] {
			cout -= A[i]
		} else {
			cout = W[1] - A[i]
			ans++
		}
		if i == W[0]-1 {
			ans++
		}
	}
	fmt.Println(ans)
}
