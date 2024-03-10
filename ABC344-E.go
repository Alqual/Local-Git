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

func NewStrline() []string {
	sc.Scan()
	return strings.Split(sc.Text(), "")
}

func main() {
	sc.Buffer(buffer, 3000000)
	N := NewInt()
	A := Newline()
	Q := NewInt()
	var N2 int = N
	var K map[int]int = map[int]int{}
	var K2 map[int]int = map[int]int{}
	for i := 0; i < N-1; i++ {
		K[A[i]] = A[i+1]
	}
	for i := 0; i < Q; i++ {
		Query := NewStrline()
		fmt.Println(Query, K)
		if Query[0] == "1" {
			di, _ := strconv.Atoi(Query[1])
			di2, _ := strconv.Atoi(Query[2])
			K[di2] = K[di]
			K2[di] = K[di2]
			K[di] = di2
			K2[di2] = di
			N2++
		} else {
			di, _ := strconv.Atoi(Query[1])
			K[di-1] = K[di]
			delete(K, di)
			N2--
		}
	}
	var i int = 0
	var j int = A[0]
	for i < N2 {
		fmt.Println(j)
		j = K[j]
		i++
	}

}
