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
	sc.Buffer(buffer, 3000000)
	W := Newline()
	A := Newline()
	if W[0] == W[1] {
		fmt.Println(-1)
	} else {
		C := make([]int, W[0])
		sort.Ints(A)
		if A[0] == 1 || A[len(A)-1] == W[0] {
			fmt.Println(-1)
		} else {
			for i := 0; i < W[0]; i++ {
				C[i] = i + 1
				if i+1 >= A[0] && i+1 <= A[len(A)-1]+1 {
					C[i]++
					if i+1 == A[len(A)-1]+1 {
						C[i] = A[0]
					}
				}
			}
			for i := 0; i < W[0]; i++ {
				fmt.Print(C[i], " ")
			}
		}
	}
}
