package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

const c = 998244353

var sc = bufio.NewScanner(os.Stdin)
var buffer = make([]byte, 10000)

func NewLine() []int {
	sc.Scan()
	ret := strings.Split(sc.Text(), " ")
	var reti []int
	for _, s := range ret {
		res, _ := strconv.Atoi(s)
		reti = append(reti, res)
	}
	return reti
}

func NewInt() int {
	sc.Scan()
	ret, _ := strconv.Atoi(sc.Text())
	return ret
}

func main() {
	sc.Buffer(buffer, 3000000)
	N := NewInt()
	A := NewLine()
	var B, E, ans int
	for i := 0; i < N; i++ {
		d := strconv.Itoa(A[i])
		s := int(math.Pow(10, float64(len(d)))) % c
		//fmt.Println(s, A[i]*s, A[i]%c)
		if i != 0 {
			B += s % c
			E += A[i] % c
			B %= c
			E %= c
		}
	}
	B *= A[0]
	B %= c
	ans = (B + E) % c
	if N >= 3 {
		for i := 1; i < N-1; i++ {
			d := strconv.Itoa(A[i])
			s := int(math.Pow(10, float64(len(d)))) % c
			r := B
			B -= s % c
			E -= A[i] % c
			B %= c
			E %= c
			ans += ((A[i]*B)%c + E) % c
			ans %= c
		}
	}
	fmt.Println(ans % c)
}
