package main

import (
	"fmt"
	"strconv"
)

func bigint_to_string(digit []int) string {
	N := len(digit)
	var str string
	for i := 0; i < N; i++ {
		str += strconv.Itoa(digit[i]) + string('0')
	}
	return str

}

func main() {
	var N int
	fmt.Scan(&N)
	digit := make([]int, N)
	for j := 0; j < N; j++ {
		fmt.Scan(&digit[j])
	}
	fmt.Println(bigint_to_string(digit))
}
