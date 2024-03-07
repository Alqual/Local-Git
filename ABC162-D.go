package main

import "fmt"

type color struct {
	r map[int]int
	g map[int]int
	b map[int]int
}

func main() {
	var S string
	var N int
	fmt.Scan(&N, &S)
	var count int = 1
	var cmap color = color{make(map[int]int), make(map[int]int), make(map[int]int)}

	for i := 0; i < N; i++ {
		if cmap.r == nil {
			cmap.r[0] = 0
			cmap.g[0] = 0
			cmap.b[0] = 0
		}
		if i > 0 {
			cmap.r[i] = cmap.r[i-1]
			cmap.g[i] = cmap.g[i-1]
			cmap.b[i] = cmap.b[i-1]
		}
		switch S[i] {
		case 'R':
			cmap.r[i]++
		case 'G':
			cmap.g[i]++
		case 'B':
			cmap.b[i]++
		}
	}
	//fmt.Println(cmap.r, cmap.g, cmap.b)
	if N <= 2 {
		fmt.Println(0)
	} else {
		count *= cmap.r[N-1] * cmap.g[N-1] * cmap.b[N-1]
		//fmt.Println(count)
		for i := 1; i <= N; i++ {
			for j := i + 2; j <= N; j++ {
				fmt.Println(i, j, (i+j)/2, S[i-1], S[j-1], S[(i+j)/2-1], count)
				if ((i+j)%2 == 0) && (S[i-1] != S[j-1]) && (S[i-1] != S[(i+j)/2-1]) && (S[j-1] != S[(i+j)/2-1]) {
					count--
				}
			}
		}
	}
	fmt.Println(count)
}
