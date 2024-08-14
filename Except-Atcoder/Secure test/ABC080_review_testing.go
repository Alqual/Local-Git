package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// Test用コードとしてレビュー版を作成
// Test用と本番の違い
// Test用 --- 現在のTest環境に沿った用語の使い方が望ましい
// 本番用 --- メンテ時の環境に沿った用語の使い方が望ましい
// Test環境から本番及びメンテ環境に行くことを想定して、変換がしやすければ、
// 全然違ったコードでも良い。

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
	Ret_num, _ := strconv.Atoi(sc.Text())
	return Ret_num
}

func calculation() {

}

//func main() {

//callした各関数の処理を制御することに特化したコードが望ましい??
//module制御??


//}


func main() { //CICDを考えるなら、mainとして長すぎでは??分離すべき
	//main関数の役割はそもそも何?? -> entry関数であり, entry関数として
	//最低限必要な機能のみ備えているべき
	//↓↓↓ entry関数というよりengineという印象
	Buf_io.buffer(Buf_init_array, Buf_max_size)
	Shopcounts := Input_Int() 
	var Shop_run_time [][]int = [][]int{} // [shopid,timezone (timezone at weekday, odd:day, even:night)]
	var Profit_shops [][]int= [][]int{} //[shopid, sink running zones]
	var Max_profit_array []int = []int{}
	var Max_profit int = 0


	for shop_id := 1; shop_id <= Shopcounts ; shop_id++{
		Shop_run_time = append(Shop_run_time, Input_list())
	}
	for shop_id := 1; shop_id <= Shopcounts; shop_id++ { 
		Profit_shops = append(Profit_shops, Input_list())
	}


	fmt.Println(Shop_run_time, Profit_shops, Shop_run_time[0][1]) 
	for timezone := 0; timezone < Maxtimezone; timezone++ {
			for shops := 0; shops < Shopcounts; shops++ { 
		
				if Shop_run_time[shops][timezone] == 1 {
					Max_profit_array[timezone] += Profit_shops[shops][timezone]
				}
			}
	}
	//Arrange Max_profit_array by disorder
	for timezone := 0; timezone < Maxtimezone; timezone++ {
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
