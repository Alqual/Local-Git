package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var (
	sc = bufio.NewScanner(os.Stdin)
	wt = bufio.NewWriter(os.Stdout)
)

const (
	inf = 1 << 60
	MOD = 998244353
)

func main() {
	/*** INIT ***/
	defer wt.Flush()
	sc.Buffer([]byte{}, inf)
	sc.Split(bufio.ScanWords)

	n := InputInt()
	a, b := make([]int, n), make([]int, n)
	acount, bcount := make([]int, n), make([]int, n)
	aseen, bseen := make(map[int]bool), make(map[int]bool)
	avals, bvals := make([]int, 0, n), make([]int, 0, n)
	for i := 0; i < n; i++ {
		a[i] = InputInt()
		if aseen[a[i]] == false {
			aseen[a[i]] = true
			avals = append(avals, a[i])
		}
		acount[i] = len(aseen)
	}
	for i := 0; i < n; i++ {
		b[i] = InputInt()
		if bseen[b[i]] == false {
			bseen[b[i]] = true
			bvals = append(bvals, b[i])
		}
		bcount[i] = len(bseen)
	}

	diff := make([]int, n)
	mp := make(map[int]bool)
	loopsize := Min(len(aseen), len(bseen))
	for i := 0; i < loopsize; i++ {
		if mp[avals[i]] == true {
			delete(mp, avals[i])
		} else {
			mp[avals[i]] = true
		}
		if mp[bvals[i]] == true {
			delete(mp, bvals[i])
		} else {
			mp[bvals[i]] = true
		}
		diff[i] = len(mp)
	}

	q := InputInt()
	for q > 0 {
		q--
		x, y, flag := InputInt(), InputInt(), true
		x--
		y--
		if acount[x] != bcount[y] {
			flag = false
		}
		k := acount[x]
		if diff[k-1] != 0 {
			flag = false
		}
		if flag {
			fmt.Fprintln(wt, "Yes")
		} else {
			fmt.Fprintln(wt, "No")
		}
	}
}

func Min(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

/*** I/O ***/
func InputInt() int {
	sc.Scan()
	val, _ := strconv.Atoi(sc.Text())
	return val
}

func InputString() string {
	sc.Scan()
	return sc.Text()
}

func OutInt(val int) {
	fmt.Fprintln(wt, val)
}

func OutString(s string) {
	fmt.Fprintln(wt, s)
}
