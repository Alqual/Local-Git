package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

var Buf_io = bufio.NewScanner(os.Stdin)

const Buf_init_size = 10000
const Buf_max_size = 3000000
const Maxtimezone = 10

type dim2 struct {
	x int
	y int
}

var Buf_Init_array = make([]byte, Buf_init_size)

//

func Input_list() []int { // function vals are OK for this simple names?
	Buf_io.Scan()
	Tmp_split_array := strings.Split(Buf_io.Text(), " ")
	Ret_list := make([]int, len(Tmp_split_array))
	for ind, strings := range Tmp_split_array {
		Ret_list[ind], _ = strconv.Atoi(strings)
	}
	return Ret_list
}

func Input_Int() int {
	Buf_io.Scan()
	Ret_num, _ := strconv.Atoi(Buf_io.Text())
	return Ret_num
}

func GetBit(n int, pos int) int {
	// 指定したビット位置の値を取得
	return int((n >> pos) & 1)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	Buf_io.Buffer(Buf_Init_array, Buf_max_size)
	Input_Ints := Input_Int()
	Input_lists := Input_list()
	sort.Ints(Input_lists)
	for Input_lists[0] != 1 {
		//fmt.Println(Input_lists)
		for i := 1; i < Input_Ints; i++ {
			if Input_lists[i] != Input_lists[0] {
				if Input_lists[i]%Input_lists[0] != 0 {
					Input_lists[i] = Input_lists[i] % Input_lists[0]
				} else {
					Input_lists[i] = Input_lists[0]
				}
			}
		}
		sort.Ints(Input_lists)
		if Input_lists[0] == Input_lists[Input_Ints-1] {
			break
		}
	}
	fmt.Println(Input_lists[0])
}
