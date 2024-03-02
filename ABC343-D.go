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
	var user map[int]int = map[int]int{}
	var count map[int]int = map[int]int{}
	var ans []int
	for i := 0; i < W[0]; i++ {
		user[i] = 0
		count[0] = W[0]
	}

	for i := 0; i < W[1]; i++ {
		C := Newline()
		C[0]--
		if count[user[C[0]]] > 0 {
			count[user[C[0]]]--
		}
		if count[user[C[0]]] == 0 {
			delete(count, user[C[0]])
		}
		user[C[0]] += C[1]
		count[user[C[0]]]++
		ans = append(ans, len(count))
		//fmt.Println(len(count), count, user)
	}
	for i := 0; i < len(ans); i++ {
		fmt.Println(ans[i])
	}
}
