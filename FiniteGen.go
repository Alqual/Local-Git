package main

import (
	"fmt"
)

type key struct {
	x, y int
}

type Numeric interface {
	int | key
}

func genRing(n int) []int {
	var ret []int
	for i := 0; i < n; i++ {
		ret = append(ret, i)
	}
	return ret
}

func gendsum(x, y int) []key {
	var ret []key
	for i := 0; i < x; i++ {
		for j := 0; j < y; j++ {
			ret = append(ret, key{i, j})
		}
	}
	return ret
}

func gendadd(n, m int) func(key1, key2 key) key {
	return func(key1, key2 key) key {
		return key{(key1.x + key2.x) % n, (key1.y + key2.y) % m}
	}
}

func gendmul(n, m int) func(key1, key2 key) key {
	return func(key1, key2 key) key {
		return key{(key1.x * key2.x) % n, (key1.y * key2.y) % m}
	}
}

func gendaddA(n int) func(key1 int, key2 key) key {
	return func(key1 int, key2 key) key {
		return key{(key1 + key2.x) % n, (key1 + key2.y) % n}
	}
}

func gendmulA(n, m int) func(key1 int, key2 key) key {
	return func(key1 int, key2 key) key {
		return key{(key1 * key2.x) % n, (key1 * key2.y) % m}
	}
}

type testdata struct {
	A []int
	R []key
}

type testaction struct {
	fnA func(int, key) key
	fnR func(key, key) key
	fnC func(int, int) int
	fnD func(int, int) int
}

func lindtest(input testdata, act testaction) bool {
	for _, a := range input.A {
		for _, b := range input.A {
			for _, x := range input.R {
				for _, y := range input.R {
					s1 := act.fnA(a, act.fnR(x, y))
					s2 := act.fnR(act.fnA(a, x), act.fnA(a, y))
					s3 := act.fnA(act.fnA(a, key{b, b}).x, x)
					s4 := act.fnA(a, act.fnA(b, x))
					s5 := act.fnA(key{1, 1}.x, x)
					if (s1 != s2) || (s3 != s4) || (s5 != x) {
						fmt.Println(s1 != s2, s3 != s4, s5 != x)
						return false
					}
				}
			}
		}
	}
	return true
}

func main() {
	var N, M, L, Q int
	_, err := fmt.Scan(&N, &M, &L, &Q)
	hello()
	for err == nil {
		var testdata testdata
		testdata.A = genRing(N)    //Nの剰余群としての可換環A
		testdata.R = gendsum(M, L) //Mの剰余群とLの剰余群の直和としてのAbel群
		var testaction testaction
		testaction.fnA = gendaddA(N)   //Nの剰余環を係数環としたときの加法
		testaction.fnR = gendmul(M, L) //Mの剰余群とLの剰余群の直和に対する乗法
		//確かめたいこと:MとLの剰余群の直和をNの剰余環に対するA-加群とみなしたときの線形性テスト
		//memo:
		//可換環の加法は直和としての剰余群の加法と異なる。また、乗法は直和としての剰余群の乗法も異なる。
		//そのため、それぞれの剰余群の直和に対する加法と乗法を再定義する必要がある。
		//memo2;
		//A-加群の構成法は、多分、Aの要素からなる部分群について、Aの加法を再定義することが一般的なのかもしれない。
		//今の方法は、Aの要素を直和の要素に対して乗法を定義することで、全く関係のない直和群の変化としてのA-加群を構成している。

		Get_lin := lindtest(testdata, testaction)

		fmt.Println("test parameter:\n", "Ring num is", N, "Abel num is", M, "\n", "mul num is", L, "add num is", Q)
		fmt.Println("Result of linearity test = ", Get_lin) //線形性のテスト結果
		//if Get_lin == true {
		//Finitegen := genfin(A_Abel_M, ARing)
		//fmt.Println("Result of finite generation = ", Finitegen) //有限生成の結果
		//}
		_, err = fmt.Scan(&N, &M, &L, &Q)
	}
	fmt.Println(err, "error")
	fmt.Println("Hello, playground")
}
