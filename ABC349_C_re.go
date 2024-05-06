package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)
var buffer = make([]byte, 10000)

func Newstring() string {
	sc.Scan()
	return sc.Text()
}

func main() {
	sc.Buffer(buffer, 3000000)
	S := Newstring()
	T := Newstring()
	T = strings.ToLower(T)
	var i, j int = 0, 0
	for (i < len(S)) && (j < 3) {
		if S[i] == T[j] {
			j++
		}
		i++
	}
	if j == 3 {
		fmt.Println("Yes")
	} else if string(T[2]) == "x" && j == 2 {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
