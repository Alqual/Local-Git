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

func gcd(x, y int) int {
	for y > 0 {
		x, y = y, x%y
	}
	return x
}

func lcm(x, y int) int {
	return x * y / gcd(x, y)
}

func main() {
	sc.Buffer(buffer, 3000000)
	N := NewInt()
	A := Newline()
	var ans, c int
	var lcms, lcms2 int
	sort.Ints(A)
	lcms = A[0]
	ans++
	if N == 1 {
		ans = 0
	} else {
		for i := 1; i < N; i++ {
			lcms2 = lcm(lcms, A[i])
			if A[i] == A[0] {
				c++
			}
			if lcms2/lcms == A[i] {
				ans++
			} else {
				for j := 0; j <= i-1; j++ {
					if A[i]%A[j] == 0 {
						break
					}
					if j == i-1 {
						ans++
					}
				}
			}
			lcms = lcms2
		}
	}
	if c == N-1 {
		ans = 0
	}
	fmt.Println(ans)
}
