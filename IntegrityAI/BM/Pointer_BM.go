package main

import (
	"fmt"
	"time"
)

func pointBM1(vars []int) map[int]int {
	var res map[int]int = map[int]int{}
	for i := range vars {
		res[i]++
	}
	var c int = 0
	for i := range res {
		c++
		if c < 2 {
			fmt.Println(i, res[i], len(res))
		}
	}
	//fmt.Println(res)
	return res
}

func pointBM2(vars []int) map[int]int {
	var res map[int]int = map[int]int{}
	vars2 := &vars
	for i := range *vars2 {
		res[i]++
	}
	var c int = 0
	for i := range res {
		c++
		if c < 2 {
			fmt.Println(i, res[i], len(res))
		}
	}
	return res
}

func pointBM3(vars []int) *map[int]int {
	var res map[int]int = map[int]int{}
	for i := range vars {
		test := i
		res[test]++
	}
	var c int = 0
	for i := range res {
		c++
		if c < 2 {
			fmt.Println(i, res[i], len(res))
		}
	}
	//fmt.Println(res)
	res2 := &res
	return res2
}

func pointBM4(vars []int) *map[int]int {
	var res map[int]int = map[int]int{}
	vars2 := &vars
	for i := range *vars2 {
		res[i]++
	}
	var c int = 0
	for i := range res {
		c++
		if c < 2 {
			fmt.Println(i, res[i], len(res))
		}
	}
	//fmt.Println(res)
	res2 := &res
	return res2
}

func main() {
	var N int = 1 << 20
	var vars []int = []int{}
	for i := 0; i < N; i++ {
		vars = append(vars, i)
	}

	// BM test //

	start1 := time.Now()                                          //現在時刻を計測
	pointBM1(vars)                                                //関数を実行
	elapsed1 := time.Since(start1)                                //秒単位で現在時刻との差分を計測
	print("N=", N, " ", "1st case = ", elapsed1.Seconds(), "s\n") //secondsとして出力

	start2 := time.Now()                                          //現在時刻を計測
	pointBM2(vars)                                                //関数を実行
	elapsed2 := time.Since(start2)                                //秒単位で現在時刻との差分を計測
	print("N=", N, " ", "2nd case = ", elapsed2.Seconds(), "s\n") //secondsとして出力

	start3 := time.Now()                                          //現在時刻を計測
	pointBM3(vars)                                                //関数を実行
	elapsed3 := time.Since(start3)                                //秒単位で現在時刻との差分を計測
	print("N=", N, " ", "3rd case = ", elapsed3.Seconds(), "s\n") //secondsとして出力

	start4 := time.Now()                                          //現在時刻を計測
	pointBM4(vars)                                                //関数を実行
	elapsed4 := time.Since(start4)                                //秒単位で現在時刻との差分を計測
	print("N=", N, " ", "4th case = ", elapsed4.Seconds(), "s\n") //secondsとして出力

}
