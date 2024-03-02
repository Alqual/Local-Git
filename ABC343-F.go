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

func main() {
	sc.Buffer(buffer, 3000000)
	W := Newline()
	A := Newline()
	B := make([]int, W[0])
	B = A
	sort.Ints(B)
	fmt.Println(B, A)

}
