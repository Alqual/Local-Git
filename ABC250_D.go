package main

import (
	"fmt"
	"math"
)

func primelist(n int) []int {
	prime := make([]int, 0)
	isprime := make([]bool, n+1)
	for i := 0; i <= n; i++ {
		isprime[i] = true
	}
	isprime[0] = false
	isprime[1] = false
	for i := 2; i <= n; i++ {
		if isprime[i] {
			prime = append(prime, i)
			for j := 2 * i; j <= n; j += i {
				isprime[j] = false
			}
		}
	}
	return prime

}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	var N, count int
	fmt.Scan(&N)
	//fmt.Println(primelist(int(math.Cbrt(float64(N)))))
	primes := primelist(int(math.Cbrt(float64(N))))
	for i := 1; i < len(primes); i++ {
		if N < primes[i]*primes[i]*primes[i] {
			//		fmt.Println("out", primes[i])
			break
		}
		//	fmt.Println("in", primes[i])
		d := N / (primes[i] * primes[i] * primes[i])
		primes2 := primelist(int(float64(min(d, primes[i]-1))))
		//	fmt.Println(primes2)
		count += len(primes2)
	}
	fmt.Println(count)
}
