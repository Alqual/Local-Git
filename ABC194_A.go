package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// stdio //////////////
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
	C := Newline() //A B
	if C[0]+C[1] >= 15 && C[1] >= 8 {
		fmt.Println(1)
	} else if C[0]+C[1] >= 10 && C[1] >= 3 {
		fmt.Println(2)
	} else if C[0]+C[1] >= 3 {
		fmt.Println(3)
	} else {
		fmt.Println(4)
	}

}
