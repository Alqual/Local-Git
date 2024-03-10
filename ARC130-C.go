package main

import (
	"fmt"
	"sort"
	"strconv"
)

func main() {
	var a, b string
	var resa, resb, ansa, ansb []int
	var resa2, resb2 []int
	fmt.Scan(&a, &b)
	for i := 0; i < len(a); i++ {
		v, _ := strconv.Atoi(string(a[i]))
		resa = append(resa, v)
	}
	for i := 0; i < len(b); i++ {
		r, _ := strconv.Atoi(string(b[i]))
		resb = append(resb, r)
	}
	sort.Ints(resa)                              //大きい方を降順
	sort.Sort(sort.Reverse(sort.IntSlice(resb))) //短い方を昇順
	var i, j int = 0, 0
	for i < len(a) && j < len(b) {
		if resa[i]+resb[j] > 10 {
			ansa = append(ansa, resa[i])
			ansb = append(ansb, resb[j])
			i++
		} else {
			resb2 = append(resb2, resb[j])
		}
		j++

	}

	fmt.Println(resa, resb)
}
