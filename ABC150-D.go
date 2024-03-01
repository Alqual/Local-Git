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

func gcd(x, y int) int {
	if y == 0 {
		return x
	}
	return gcd(y, x%y)
}

func two(x int) int {
	var ans int
	for x%2 == 0 {
		x /= 2
		ans++
	}
	return ans
}

func two2(x int) int {
	for x%2 == 0 {
		x /= 2
	}
	return x
}

func main() {
	sc.Buffer(buffer, 3000000)
	W := Newline()
	a := Newline()
	var lcm int
	lcm = 1
	for i := 0; i < W[0]; i++ {
		if i != 0 && (two(a[i]) != two(lcm)) {
			lcm = 0
			break
		}
		lcm *= (a[i] / gcd(a[i], lcm))
	}
	if lcm != 0 {
		W[1] /= (lcm / two2(lcm))
		lcm = two2(lcm)
		//fmt.Println(lcm, W[1])
		if lcm > W[1] {
			fmt.Println(0)
		} else {
			fmt.Println(W[1]/lcm + 1)
		}
	} else {
		fmt.Println(0)
	}
}
