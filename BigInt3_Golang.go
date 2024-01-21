package main

import "fmt"

func max(x int, y int) int {
	if x < y {
		return y
	} else {
		return x
	}
}

func carry_and_fix(digit []int) []int {
	N := len(digit)
	digit2 := make([]int, N)
	digit2 = digit
	K := 0

	for i := int(0); i < N-1; i++ {
		// 繰り上がり処理 (K は繰り上がりの回数)
		if digit[i] >= 10 {
			K = digit[i] / 10
			digit2[i] -= K * 10
			digit2[i+1] += K
		}
		// 繰り下がり処理 (K は繰り下がりの回数)
		if digit[i] < 0 {
			K = (-digit[i]-1)/10 + 1
			digit2[i] += K * 10
			digit2[i+1] -= K
		}
	}
	// 一番上の桁が 10 以上なら、桁数を増やすことを繰り返す
	for digit2[len(digit2)-1] >= 10 {
		K = digit2[len(digit2)-1] / 10
		digit2[len(digit2)-1] -= K * 10
		digit2 = append(digit2, K)
	}
	// 1 桁の「0」以外なら、一番上の桁の 0 (リーディング・ゼロ) を消す
	for len(digit2) >= 2 && digit2[len(digit2)-1] == 0 {
		digit2 = digit2[:len(digit2)-2]
	}
	return digit2

}

func addition(digit_a []int, digit_b []int) []int {
	N := max(len(digit_a), len(digit_b)) // a と b の大きい方
	digit_ans := make([]int, N)          // 長さ N の配列 digit_ans を作る
	for i := int(0); i < N; i++ {
		if i < len(digit_a) {
			digit_ans[i] = digit_a[i]
		} else {
			digit_ans[i] = 0
		}
		if i < len(digit_b) {
			digit_ans[i] += digit_b[i]
		}
		// digit_ans[i] を digit_a[i] + digit_b[i] にする (範囲外の場合は 0)
	}

	return carry_and_fix(digit_ans)

}

func main() {
	var N int
	fmt.Scan(&N)
	digit_a := make([]int, N)
	digit_b := make([]int, N)
	digit := make([]int, N)
	fmt.Println("digit_a = \n")
	for i := 0; i < N; i++ {
		fmt.Scan(&digit_a[i])
	}
	fmt.Println("digit_b = \n")
	for i := 0; i < N; i++ {
		fmt.Scan(&digit_b[i])
	}

	for j := 0; j < len(digit); j++ {
		fmt.Println(digit[j])
	}
	digit = addition(digit_a, digit_b)
	fmt.Println("digit_a,digit_b =\n", digit_a, digit_b)
	fmt.Println("digit_a + digit_b = \n")
	for j := 0; j < N; j++ {
		fmt.Println(digit[j])
	}
}
