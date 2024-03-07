package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)

func Newline() []int {
	sc.Scan()
	arr := strings.Split(sc.Text(), " ")
	ret := make([]int, len(arr))
	for i, v := range arr {
		ret[i], _ = strconv.Atoi(v)
	}
	return ret
}

func main() {
	var ans int
	W := Newline()
	A := Newline()
	sc.Scan()
	T := strings.Split(sc.Text(), "")

	sort.Sort(sort.Reverse(sort.IntSlice(A)))
	var maps map[string]int = map[string]int{"r": A[0], "s": A[1], "p": A[2]}
	var maps2 map[string]string = map[string]string{"r": "p", "s": "r", "p": "s"}
	var maps3 map[string]string = map[string]string{"r": "s", "s": "p", "p": "r"}
	if W[0] < W[1] {
		for i := 0; i < W[0]; i++ {
			if string(T[i]) == "r" {
				ans += maps["p"]
			} else if string(T[i]) == "s" {
				ans += maps["r"]
			} else {
				ans += maps["s"]
			}
		}
	} else {
		var res []string
		for i := 0; i < W[0]; i++ {
			if i < W[1] {
				ans += maps[maps2[string(T[i])]]
				res = append(res, maps2[string(T[i])])
			} else {
				//fmt.Println(res, ans, maps2[string(T[i])])
				if string(T[i]) != string(T[i-W[1]]) {
					ans += maps[maps2[string(T[i])]]
					res = res[1:]
					res = append(res, maps2[string(T[i])])
				} else {
					if res[0] == maps2[string(T[i])] {
						res = res[1:]
						res = append(res, maps3[string(T[i])])
					} else {
						ans += maps[maps2[string(T[i])]]
						res = res[1:]
						res = append(res, maps2[string(T[i])])
					}
				}
			}
		}
	}
	fmt.Println(ans)
}
