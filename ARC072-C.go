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

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func main() {
	n := NewInt()
	a := Newline()
	var ans, sum int
	sum = a[0]
	for i := 1; i < n; i++ {
		if sum > 0 {
			ans += (sum + a[i])
			a[i] = -1 - sum
			sum = -1
		} else if sum < 0 {
			ans += 1 - sum - a[i]
			a[i] = 1 - sum
			sum = 1
		}
	}
	fmt.Println(ans)
}
