package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)

func Newline() []int {
	sc.Scan()
	input := strings.Split(sc.Text(), " ")
	var result []int
	for _, v := range input {
		arr, _ := strconv.Atoi(v)
		result = append(result, arr)
	}
	return result
}

func NewInt() int {
	sc.Scan()
	input, _ := strconv.Atoi(sc.Text())
	return input
}

func main() {
	N := NewInt()
	A := Newline()
	var res map[int]int = map[int]int{}
	for i := 0; i < N-1; i++ {
		res[A[i]]++
	}
	for i := 1; i <= N; i++ {
		fmt.Println(res[i])
	}
}
