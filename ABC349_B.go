package main

import "fmt"

func main() {
	var S string
	fmt.Scan(&S)
	var cout map[int]int = map[int]int{}
	var maps map[string]int = map[string]int{}
	var ans string = "Yes"
	for i := 0; i < len(S); i++ {
		maps[string(S[i])]++
	}
	for i := range maps {
		cout[maps[i]]++
	}
	for i := range cout {
		if (cout[i] != 2) && (cout[i] != 0) {
			ans = "No"
			break
		}
	}
	fmt.Println(ans)
}
