package main

import (
	"bufio"
	"fmt"
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
func NewInt() int {
	sc.Scan()
	ret, _ := strconv.Atoi(sc.Text())
	return ret
}

func NewWord() string {
	sc.Scan()
	return sc.Text()
}

func NewStrline() []string {
	sc.Scan()
	return strings.Split(sc.Text(), "")
}

type Key struct {
	X, Y int
}

func main() {
	sc.Buffer(buffer, 3000000)
	T := NewWord()
	N := NewInt()
	var DP1 map[Key]bool = map[Key]bool{}
	var DP2 map[Key]int = map[Key]int{}
	var Dp3 map[int][]int = map[int][]int{}
	var ans int
	for i := 1; i <= N; i++ {
		K := NewStrline()
		for j := 1; j <= len(K); j++ {
			if i == 1 {
				if T[:len(K[j-1])] == K[j-1] {
					DP1[Key{1, len(K[j-1])}] = true
					DP2[Key{1, len(K[j-1])}]++
					Dp3[1] = append(Dp3[1], len(K[j-1]))
				}
				fmt.Println(DP1, DP2, Dp3)
			} else {
				for _, v := range Dp3[i-1] {
					if T[v:v+len(K[j-1])] == K[j-1] {
						DP1[Key{i, v + len(K[j-1])}] = true
						DP2[Key{i, v + len(K[j-1])}] += DP2[Key{i - 1, v}]
						Dp3[i] = append(Dp3[i], v+len(K[j-1]))
						if v+len(K[j-1]) == len(T) {
							if ans == 0 {
								ans = DP2[Key{i, v + len(K[j-1])}]
							} else if ans > DP2[Key{i, v + len(K[j-1])}] {
								ans = DP2[Key{i, v + len(K[j-1])}]
							}
						}
					}
				}
			}
		}
	}
	fmt.Println(ans)
}
