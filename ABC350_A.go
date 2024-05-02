package main

import (
	"fmt"
	"strconv"
)

func main() {
	var S string
	fmt.Scan(&S)
	d := string(S[3:6])
	ints, _ := strconv.Atoi(d)
	if ints < 350 && ints != 316 && ints != 0 {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
