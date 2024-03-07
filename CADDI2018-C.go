package main

import "fmt"

const v_ = 1000000000000

var s = cal(v_, 2)

var store int

func cal(x, y int) int {
	var ans int = 0
	for x%y == 0 {
		ans++
		x /= y
	}
	store = x
	return ans
}

func cal2(x, y int) int {
	var ans int = x
	for ans%y == 0 {
		ans /= y
	}
	return ans

}

func cal3(x, y int) int {
	var ans int = 1
	for i := 1; i <= y; i++ {
		ans *= x
	}
	return ans
}

func main() {
	var N, P, ans int
	fmt.Scan(&N, &P)

	var k int = 2
	ans = 1

	for P >= cal3(k, N) {
		cals := cal(P, k)
		if cals >= N {
			ans *= cal3(k, cals/N)
			P = store
		} else if (P%k == 0) && cals < N {
			P = store
		}
		if k == 2 {
			k++
		} else {
			k += 2
		}
	}
	fmt.Println(ans)
}
