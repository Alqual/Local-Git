package main

import (
	"bufio"
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
	Input_lists_Num := Input_list()
	camel_weigh := Input_list()
	sort.Ints(camel_weigh)
	var blid_len []int = []int{}
	var blid_weigh []int = []int{}
	var max_camel []int = []int{}
	var dum int
	for i := 0; i < Input_lists_Num[1]; i++ {
		Input_lists_pair := Input_list()
		blid_len, blid_weigh = append(blid_len, Input_lists_pair[0]), append(blid_weigh, Input_lists_pair[1])
	}
	for j := 0; j < Input_lists_Num[1]; j++ {
		dum = 0
		for k := 0; k < Input_lists_Num[0]; k++ {
			dum += camel_weigh[k]
			if dum > blid_weigh[j] {
				max_camel = append(max_camel, k+1)
				break
			}
		}
	}

}
