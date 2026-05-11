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
	sc.Buffer(buffer, 3000000)
	W := Newline()
	D := Newline()
	K := W[1] + W[2]
	var Cmin, Cmax int
	for i := 0; i < W[0]; i++ {
		if i == 0 {
			Cmin = D[i] % K
			Cmax = D[i] % K
		} else {
			if Cmin > D[i]%K {
				Cmin = D[i] % K
			}
			if Cmax < D[i]%K {
				Cmax = D[i] % K
			}
		}
	}
	if Cmax-Cmin >= W[1] || Cmin >= W[2] {
		fmt.Println("No")
	} else {
		fmt.Println("Yes")
	}
}
