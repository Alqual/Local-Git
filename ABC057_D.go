package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

var sc = bufio.NewScanner(os.Stdin)
var buffer = make([]byte, 10000)

func Newline() []int {
	sc.Scan()
	ret := strings.Split(sc.Text(), " ")
	var reti []int
	for _, s := range ret {
		res, _ := strconv.Atoi(s)
		reti = append(reti, res)
	}
	return reti
}

func main() {
	W := Newline() //N A B
	V := Newline() //v1 v2 ... vn
	sort.Ints(V)
	var sum, cns, cns2 int
	for i := W[0] - 1; i >= 0; i-- {
		if i > W[0]-W[1] {
			sum += V[i]
			cns2++
		} else if i == W[0]-W[1] {
			sum += V[i]
			cns++
			cns2++
		} else {
			if (float64(sum)/float64(cns2) == float64(sum+V[i])/float64(cns2+1)) && cns2 <= W[2] {
				sum += V[i]
				cns2++
				cns++
			} else if V[i] == V[W[0]-W[1]] {

			} else {
				break
			}
		}
	}
	fmt.Println(float64(sum)/float64(cns2), cns)
}
