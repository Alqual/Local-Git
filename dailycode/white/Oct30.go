// 10分10行1機能コード
// func以下行について10行とする
// 行数はできる限り短くする
package main

func minvalue(a []int) (int, int) { //配列から最小値とその位置を返す関数
	min := a[0]
	min2 := 0
	for ind, v := range a {
		if v < min {
			min = v
			min2 = ind
		}
	}
	return min, min2 + 1
}
