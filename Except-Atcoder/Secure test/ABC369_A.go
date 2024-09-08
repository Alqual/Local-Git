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

func main() {
	Buf_io.Buffer(Buf_Init_array, Buf_max_size)
	Input_lists := Input_list()
	if Input_lists[0] == Input_lists[1] {
		fmt.Println(1)
	} else {
		if (Input_lists[0]-Input_lists[1])%2 == 0 {
			fmt.Println(3)
		} else {
			fmt.Println(2)
		}
	}
}
