package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// codeのタイプによって、コードの可用性は異なって良い。今回のは本番用なので、メンテナンス性を重視したレビューとしてる


var Buf_io = bufio.NewScanner(os.Stdin) // what means this operation?
// more describtive name is better, Scan_start is a little simple
const Buf_init_size = 10000
const Buf_max_size = 300000
var Buf_Init_array = make([]byte, Buf_init_size)
//
func Input_list() []int { // function vals are OK for this simple names?
	Buf_io.Scan()
	Tmp_split_array := strings.Split(Buf_io.Text(), " ") // arr is not good ?
	Ret_list := make([]int, len(Tmp_split_array))
	for ind, strings := range Tmp_split_array {
		Ret_list[ind], _ = strconv.Atoi(strings)
	}
	return Ret_list
}

func Input_Int() int {
	Buf_io.Scan()
	Ret_num, _ := strconv.Atoi(sc.Text())
	return Ret_num
}

func main() {
	Buf_io.buffer(Buf_init_array, Buf_max_size)
	N := Input_Int() //NewInt is not clear. should be more describetive name
	//var F, P [][]int = [][]int{}, [][]int{} // what is F, and P ?
	var Shop_run_time [][]int = [][]int{} // [shopid,timezone (timezone at weekday, odd:day, even:night)]
	var Profit_shops [][]int= [][]int{} //[shopid, sink running zones]
	//Shortcut form (in this case, F and P are parallelly called) is difficult?
	var ans, co, min int = 0, 0, 0 // Is this op really necessary?
	var Max_profit_array []int = []int{}
	var Max_profit int = 0

	co2 := make([]int, N) //??? corbon dioxide?


	for shop_id := 1; shop_id <= N ; shop_id++{
		Shop_run_time = append(Shop_run_time, Input_list())
	}
	for shop_id := 1; shop_id <= N; shop_id++ { // i is not clear. what it is for? counting some?		F = append(F, Newline())
		// same loop vals makes confusion which gives loops
		Profit_shops = append(Profit_shops, Input_list()) //  what is P ?
	}


	fmt.Println(Shop_run_time, Profit_shops, Shop_run_time[0][1]) // is matrix necessary? normally matrix is more cost
	for timezone := 0; timezone < 10; timezone++ {
			for shops := 0; shops < N; shops++ { // other loop, using "j" is no so much bad, but even though a little not clear
		
				if Shop_run_time[shops][timezone] == 1 {
					Max_profit_array[timezone] += Profit_shops[shops][timezone]
				}
			}
	}

//Arrange Max_profit_array by disorder
for timezone := 0; timezone < 10; timezone++ {
	if timezone == 0 && Max_profit_array[timezone] <0{
		Max_profit = Max_profit_array[0]
		break
	}
	if Max_profit_array[timezone]=<0{
		break
	}
	Max_profit+=Max_profit_array[timezone]
}
	fmt.Println(Max_profit)
}
