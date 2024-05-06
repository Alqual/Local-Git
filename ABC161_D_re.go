package main

import (
	"fmt"
	"sort"
	"strconv"
)

var res0 []int = []int{}

func step(chk, s, K10, num int, maps map[int][]int) {
	if chk <= K10 {
		for _, v := range maps[s] {
			res0 = append(res0, num*10+v)
			dum := num*10 + v
			if dum == 0 {
				continue
			}
			lens := strconv.Itoa(dum)
			chk = len(lens)
			//fmt.Println("a", chk, dum, res0, v, num, s, maps[s])
			if chk <= K10 {
				step(chk, v, K10, dum, maps)
			}
		}
	}
}

func Solve(K10 int, maps map[int][]int) []int {
	for i := 1; i <= 9; i++ {
		res0 = append(res0, i)
		step(1, i, K10, i, maps)
		//fmt.Println("b", i)
	}
	return res0
}

func main() {
	var K int
	fmt.Scan(&K)
	K10 := 9
	var maps map[int][]int = map[int][]int{}
	var res []int = []int{}
	for i := 0; i <= 9; i++ {
		if i == 0 {
			maps[i] = append(maps[i], 0, 1)
		} else if i == 9 {
			maps[i] = append(maps[i], 8, 9)
		} else {
			maps[i] = append(maps[i], i-1, i, i+1)
		}
	}
	//fmt.Println(maps, K10)
	res = Solve(K10, maps)
	sort.Ints(res)
	fmt.Println(res[K-1])
}
