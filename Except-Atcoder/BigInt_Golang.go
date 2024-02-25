package main

import (
	"fmt"
	"strconv"
	"strings"
)

func str(S string) []int {
	digit := make([]int, len(S))
	for i := 0; i < len(S); i++ {
		digit[i], _ = strconv.Atoi(strings.Replace(string(S[len(S)-i-1]), "0", "", -1))

	}
	return digit
}

func main() {
	var S string
	var digit []int
	fmt.Scan(&S)
	digit = str(S)
	for j := 0; j < len(digit); j++ {
		fmt.Println(digit[j])
	}
}
