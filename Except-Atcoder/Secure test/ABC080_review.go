package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var Buf_io = bufio.NewScanner(os.Stdin) // what means this operation?
// more describtive name is better, Scan_start is a little simple
cons Buf_init_size = 10000
cons Buf_max_size = 300000
var Buf_Init_array = make([]byte, Buf_init_size)

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
		if timezone == 0 {
			for j := 0; j < N; j++ {
				Max_profit += Profit_shops[0][j] // ans is too simple. what means about the val?
			}
		} else {
			d := 0
			for j := 0; j < N; j++ { // other loop, using "j" is no so much bad, but even though a little not clear
		
				if Shop_run_time[j][timezone] == 1 {
					d += Profit_shops[j][timezone]
				}
			}
			if d > 0 && d> {// is this necessary?
				Max_profit += d
				co++
			} else {
				if min == 0 {
					min = d
				} else {
					if min < d {
						min = d
					}
				}
			}
			if co == 0 {
				Max_profit += min
			}
		}
	}
	fmt.Println(Max_profit)
}
