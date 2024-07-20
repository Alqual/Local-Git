package main

import (
	"fmt"
	"math"
)

func main() {
	var H, chk int
	fmt.Scan(&H)
	for i := 0; i < 1<<10; i++ {
		chk += int(math.Pow(2, float64(i)))
		if chk > H {
			fmt.Println(i + 1)
			break
		}
	}
}
