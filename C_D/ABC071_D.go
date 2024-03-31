package main

import "fmt"

func main() {
	var S1, S2 string
	var N int
	N = 52
	S1 = "RvvttdWIyyPPQFFZZssffEEkkaSSDKqcibbeYrhAljCCGGJppHHn"
	S2 = "RLLwwdWIxxNNQUUXXVVMMooBBaggDKqcimmeYrhAljOOTTJuuzzn"
	//fmt.Scan(&N)
	//fmt.Scan(&S1)
	//fmt.Scan(&S2)
	var ans int
	if S1[0] == S2[0] {
		ans = 3
	} else {
		ans = 6
	}
	for i := 1; i < N; i++ {
		if S1[i] != S1[i-1] {
			if S1[i-1] == S2[i-1] {
				ans *= 4
			}
		}
		ans %= 1000000007
	}
	fmt.Println(ans)
}
