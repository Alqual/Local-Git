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
	var cul map[int]bool = map[int]bool{}
	var cons []int
	for i := 0; i < N; i++ {
		A := NewInt()
		if cul[A] == true {
			delete(cul, A)
		} else {
			cul[A] = true
		}
	}
	for v, _ := range cul {
		cons = append(cons, v)
	}
	fmt.Println(len(cons))
}
