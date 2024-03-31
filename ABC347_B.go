package main

import "fmt"

func main() {
	var S string
	fmt.Scan(&S)
	var maps map[string]bool = map[string]bool{}
	for i := 0; i < len(S); i++ {
		for j := i; j < len(S); j++ {
			maps[S[i:j+1]] = true
		}
	}
	fmt.Println(len(maps))
}
