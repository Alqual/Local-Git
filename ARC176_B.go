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

func main() {
	T := NewInt()
	for i := 0; i < T; i++ {
		W := Newline()
		if W[1] == 2 && W[2] == 1 {
			fmt.Println(0)
		} else {
			P := W[0] % (W[1] - W[2])
			D := W[0] / (W[1] - W[2])
			if W[0]-(D-1)*(W[1]-W[2]) < W[1] {

			}
			if P%4 == 0 {
				fmt.Println(6)
			} else if P%4 == 1 {
				fmt.Println(2)
			} else if P%4 == 2 {
				fmt.Println(4)
			} else {
				fmt.Println(8)
			}
		}
	}
}
