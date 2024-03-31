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
	A := Newline()
	var ans int
	var cons []int
	var cul map[int]int = map[int]int{}

	for i := 0; i < N; i++ {
		cul[A[i]]++
	}
	for v, _ := range cul {
		cons = append(cons, v)
	}
	sort.Sort(sort.Reverse(sort.IntSlice(cons)))
	for k, i := range cons {
		//fmt.Println(cul, i, cons, ans)
		if cul[i] >= 2 {
			if cul[i] >= 4 && ans == 0 {
				ans = i * i
				break
			}
			if ans == 0 {
				ans = i
			} else {
				ans *= i
				break
			}
		}
		if k == len(cons)-1 {
			ans = 0
		}
	}
	fmt.Println(ans)
}
