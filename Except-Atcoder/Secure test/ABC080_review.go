package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var Scan_start = bufio.NewScanner(os.Stdin) // what means this operation?
// more describtive name is better, Scan_start is a little simple
var buffer = make([]byte, 10000)

func Input_List() []int { // function vals are OK for this simple names?
	Scan_start.Scan()
	arr := strings.Split(Scan_start.Text(), " ") // arr is not good ?
	ret := make([]int, len(arr))
	for i, v := range arr {
		ret[i], _ = strconv.Atoi(v)
	}
	return ret
}

func Input_Int() int {
	Scan_start.Scan()
	ret, _ := strconv.Atoi(sc.Text())
	return ret
}

func main() {
	N := Input_Int() //NewInt is not clear. should be more describetive name
	var F, P [][]int = [][]int{}, [][]int{} // what is F, and P ?
	//Shortcut form (in this case, F and P are parallelly called) is difficult?
	var ans, co, min int = 0, 0, 0 // Is this op really necessary?
	co2 := make([]int, N) //??? corbon dioxide?
	for i := 0; i < N; i++ { // i is not clear. what it is for? counting some?		F = append(F, Newline())
		// same loop vals makes confusion which gives loops
		P = append(P, Input_List())
	}
	fmt.Println(F, P, F[0][1]) // is matrix necessary? normally matrix is more cost
	for i := 0; i < 10; i++ {
		if i == 0 {
			for j := 0; j < N; j++ {
				ans += P[0][j] // ans is too simple. what means about the val?
			}
		} else {
			d := 0
			for j := 0; j < N; j++ { // other loop, using "j" is no so much bad, but eve
		
				if F[j][i] == 1 {
					d += P[j][i]
				}
			}
			if d > 0 && d> {// is this necessary?
				ans += d
				co++
			} else {
				if min == 0 {
					min = d
				} else {
					if min < d {
						min = d
					}
				}
			}
			if co == 0 {
				ans += min
			}
		}
	}
	fmt.Println(ans)
}
