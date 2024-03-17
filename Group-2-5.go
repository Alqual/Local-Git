package main

import (
	"fmt"
	"slices"
	"sort"
)

type key struct {
	x, y int
}

func genRing(n int) []int {
	var ret []int
	for i := 0; i < n; i++ {
		ret = append(ret, i)
	}
	return ret
}

func genadd(n int) func(int, int) int {
	return func(x, y int) int {
		return (x + y) % n
	}
}

func genmul(n int) func(int, int) int {
	return func(x, y int) int {
		return (x * y) % n
	}
}

func genfin(Abel_A []int, A []int) []int {
	var ret []int
	for _, x := range Abel_A {
		for _, a := range A {
			if a != 0 && x%a == 0 {
				ret = append(ret, x/a)
			}
		}
	}
	sort.Ints(ret)
	return slices.Compact(ret)
}

func lintest(test_A []int, test_B []int, fnA func(int, int) int, fnB func(int, int) int) bool {
	for _, a := range test_A {
		for _, b := range test_A {
			for _, x := range test_B {
				for _, y := range test_B {
					s1 := fnA(a, fnB(x, y))
					s2 := fnB(fnA(a, x), fnA(a, y))
					s3 := fnA(fnA(a, b), x)
					s4 := fnA(a, fnA(b, x))
					s5 := fnA(1, x)
					if (s1 != s2) || (s3 != s4) || (s5 != x) {
						return false
					}
				}
			}
		}
	}
	return true
}

func main() {
	//var Abel_3 []int = []int{0, 1, 2}             //3の剰余群で定義されるAbel群
	//var Abel_5 []int = []int{0, 1, 2, 3, 4}       //5の剰余群で定義されるAbel群
	var N, M, L, Q int
	_, err := fmt.Scan(&N, &M, &L, &Q)
	for err == nil {
		var ARing []int = genRing(N)    //Aに対応した可換環
		var A_Abel_M []int = genRing(M) //A-加群としてのAbel群
		mulN := genmul(L)               //Ring_Aに対する乗法
		addM := genadd(Q)               //AbelA_Mに対する加法
		Get_lin := lintest(ARing, A_Abel_M, mulN, addM)

		fmt.Println("test parameter:\n", "Ring num is", N, "Abel num is", M, "\n", "mul num is", L, "add num is", Q)
		fmt.Println("Result of linearity test = ", Get_lin) //線形性のテスト結果
		if Get_lin == true {
			Finitegen := genfin(A_Abel_M, ARing)
			fmt.Println("Result of finite generation = ", Finitegen) //有限生成の結果
		}
		_, err = fmt.Scan(&N, &M, &L, &Q)
	}
	fmt.Println(err, "error")
}
