package main

//これは間違い。DFSを使って橋の本数がM本であればYes、そうでなければNoという問題。
import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)
var buffer = make([]byte, 10000)

func nextLine() []int {
	sc.Scan()
	arr := strings.Split(sc.Text(), " ")
	ret := make([]int, len(arr))
	for i, v := range arr {
		ret[i], _ = strconv.Atoi(v)
	}
	return ret
}

func main() {
	sc.Buffer(buffer, 3000000)
	W := nextLine()
	var ans string = "Yes"
	var a, b []int
	var maps map[int]int = map[int]int{}
	var kar map[int]string = map[int]string{}
	a = nextLine()
	b = nextLine()
	for i := 0; i < W[1]; i++ {
		if maps[a[i]] == 0 {
			maps[a[i]] = 2
			kar[a[i]] = "S"
		}
		if maps[b[i]] != maps[a[i]] {
			if maps[a[i]] == 1 {
				maps[b[i]] = 2
				kar[b[i]] = "T"
			} else {
				maps[b[i]] = 1
				kar[b[i]] = "T"
			}
		} else {
			if (i == W[1]-1) || (a[i] == b[i]) {
				ans = "No"
				break
			} else if kar[a[i]] == kar[b[i]] {
				ans = "No"
				break
			} else {
				if maps[a[i]] == 1 {
					maps[b[i]] = 2
					kar[b[i]] = "T"
				} else {
					maps[b[i]] = 1
					kar[b[i]] = "T"
				}
			}
		}
		//fmt.Println(maps)
	}
	fmt.Println(ans)
}
