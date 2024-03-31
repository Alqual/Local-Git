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

func NewInt() int {
	sc.Scan()
	ret, _ := strconv.Atoi(sc.Text())
	return ret
}

func main() {
	sc.Buffer(buffer, 3000000)
	N := NewInt()
	p := Newline()
	var ans int = 0
	if N == 2 && p[0] == 1 {
		ans++
	}
	if N >= 3 {
		if p[0] == 1 {
			p[0] = p[1]
			p[1] = 1
			ans++
		}
		if p[1] == 2 {
			p[1] = p[2]
			p[2] = 2
			ans++
		}
		for i := 2; i < N; i++ {
			if p[i] == i+1 {
				ans++
			}
		}
	}
	fmt.Println(ans)
}
