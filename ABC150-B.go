package main

import (
	"bufio"
	"fmt"
	"os"
)

var sc = bufio.NewScanner(os.Stdin)

func main() {
	var N, ans int
	var S string
	fmt.Scan(&N)
	fmt.Scan(&S)
	for i := 0; i < N-2; i++ {
		//fmt.Println(string(S[i : i+3]))
		if string(S[i:i+3]) == "ABC" {
			ans++
			i += 2
		}
		if i == N-3 {
			break
		}
	}
	fmt.Println(ans)
}
