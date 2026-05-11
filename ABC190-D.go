package main

import (
	"fmt"
	"math"
)

func main() {
	var N, count int
	fmt.Scan(&N)
	N0 := int(math.Sqrt(float64(N)*2.)) + 1
	//fmt.Println(N0, 2*N)
	for i := 1; i <= N0; i++ {
		if (2*N)%i == 0 && ((2*N/i)-i)%2 == 1 {
			//fmt.Println(i, 2*N/i)
			count++
		}
	}
	fmt.Println(2 * count)
}
