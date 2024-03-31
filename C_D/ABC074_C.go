package main

import (
	"bufio"
	"os"
	"strconv"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)
var buffer = make([]byte, 10000)

func Newline() []int {
	sc.Scan()
	arr := strings.Split(sc.Text(), " ")
	ret := make([]int, len(arr))
	for i, v := range arr {
		ret[i], _ = strconv.Atoi(v)
	}
	return ret
}

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func main() {
	P := Newline()
	WM := min(100*P[0], 100*P[1])
	SM := min(P[2], P[3])
	PM := min(WM, SM)
	L := P[5] / PM
	var DPW []int = make([]int, L)
	var DPS []int = make([]int, L)
	DPW[0] = 100 * P[0]
	DPS[0] = 0
	for i := 1; i < L; i++ {
		FD:= DPS[i-1] - P[4]*DPW[i-1]/100
		SD:= DPW[i-1] + DPS[i-1]
			if SD + min(P[2], P[3]) >P[5] {
				break
			} 
			
			if FD + min(P[2], P[3]) > 0 + SD+WM<=P[5]{
			DPS[i] = DPS[i-1]
			DPW[i] = DPW[i-1]+WM
		} else if FD + max(P[2], P[3]) < 0{
			DPS[i] = DPS[i-1] + min(P[2], P[3])
			DPW[i] = DPW[i-1]
		} else {
			DPS[i] = DPS[i-1] + max(P[2], P[3])
			DPW[i] = DPW[i-1]
		}

}
