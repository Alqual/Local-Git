package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)
var buffer = make([]byte, 10000)

func Newstring() string {
	sc.Scan()
	return sc.Text()
}

func main() {
	sc.Buffer(buffer, 3000000)
	S := Newstring()
	T := Newstring()
	T = strings.ToLower(T)
	var ans int
	for i := 0; i < len(S); i++ {
		if ans == 0 {
			if S[i] == T[0] {
				ans++
			}
		} else if ans == 1 {
			if S[i] == T[1] {
				ans++
			}
		} else {
			if S[i] == T[2] {
				ans++
				break
			}
		}
	}
	//else {
	//	if string(S[i]) == strings.ToLower(string(T[2])) {
	//		ans += string(T[2])
	//		break
	//	}
	fmt.Println(ans)
	if ans == 3 || ((ans == 2) && (string(T[2]) == "x")) {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
