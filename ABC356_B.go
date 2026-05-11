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

func main() {
	W := Newline()
	A := Newline()
	Nutri := make([]int, W[1])
	for i := 0; i < W[0]; i++ {
		X := Newline()
		for j := 0; j < W[1]; j++ {
			Nutri[j] += X[j]
		}
	}
	var chk bool = false
	for i := 0; i < W[1]; i++ {
		if Nutri[i] < A[i] {
			chk = false
			break
		} else {
			chk = true

		}
	}
	//fmt.Println(Nutri, A)
	if chk {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}

}
