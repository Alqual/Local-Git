// 入力されたn組の文字列について、それぞれの部分集合の数が同じであるかを判定
// 例えば、入力が["a", "b", "c"]と["a", "b", "c", "d"]の場合、
// 部分集合の数はそれぞれ2^3=8と2^4=16で異なるため、Falseを返す
// 入力が["a", "b", "c"]と["a", "b", "c"]の場合、部分集合の数はそれぞれ2^3=8と2^3=8で同じため、Trueを返す
// 制約: 10行以内
// 結果: 書けなかった。後数行必要になった。
package main

func Oct5(input_ []string) bool {
	var check map[lune]int
	var dum, dum2 int = 0, 0
	for i := 0; i < len(input_); i++ {
		for j := 0; j < len(input_[i]); j++ {
			check[input_[i][j]]++
			dum *= (check[input_[i][j]] + 1) / check[input_[i][j]]
		}
	}
}
