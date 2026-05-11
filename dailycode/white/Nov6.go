//二つの文字列について、入力指定したm回以下の互換操作で一致するかどうかを判定する
//互換操作とは、文字列の任意の位置にある文字を他の文字に変更すること
//例えば、文字列"abc"と"adc"は、1回の互換操作で一致する
//文字列s,tと整数mが与えられるので、文字列s,tがm回以下の互換操作で一致するかどうかを判定してください

package main

func gokan(s, t string, m int) bool {
	if len(s) != len(t) {
		return false
	}
	for i := 0; i < len(s); i++ {
		if s[i] != t[i] {
			m--
		}
	}
	return m >= 0
}
