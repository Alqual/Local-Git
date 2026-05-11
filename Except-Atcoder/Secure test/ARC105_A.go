package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var Buf_io = bufio.NewScanner(os.Stdin)

const Buf_init_size = 10000
const Buf_max_size = 300000
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

func main() {
	Buf_io.Buffer(Buf_Init_array, Buf_max_size)
	Input_lists := Input_list()
	var Sum, chk, dum int
	for i := 0; i < 4; i++ {
		Sum += Input_lists[i]
	}
	for j := 0; j < 1<<4; j++ {
		for k := 1; k <= 4; k++ {
			if GetBit(j, k) == 1 {
				dum += Input_lists[k-1]
			}
		}
		if dum == Sum-dum {
			chk = 1
			fmt.Println("Yes")
			break
		}
		dum = 0
	}
	if chk == 0 {
		fmt.Println("No")
	}

}
