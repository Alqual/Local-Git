package main

import "fmt"

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func dfs(S []string, vx int, vy int, maxc int, color map[int][]int) map[int][]int {
	color[vx][vy] = maxc
	L := len(S)
	H := len(S[0])
	vx3 := max(vx-1, 0)
	vx4 := min(vx+1, L-1)
	vy3 := max(vy-1, 0)
	vy4 := min(vy+1, H-1)
	for vy3 < vy4 {
		for vx3 < vx4 {
			//fmt.Println(vx3, vy3, L, H, string(S[vx3][vy3]), color[vx3][vy3])
			if string(S[vx3][vy3]) == "#" {
				if color[vx3][vy3] != maxc && color[vx3][vy3] != 0 {
					vx3 = max(vx-1, 0)
					vy3 = max(vy-1, 0)
					maxc = color[vx3][vy3]
				} else {
					color[vx3][vy3] = maxc
				}
			}
			vx3++
		}
		vy3++
	}
	maxc++
	return color
}

func multree(S []string) map[int][]int {
	var color map[int][]int = map[int][]int{}
	L := len(S)
	H := len(S[0])
	maxc := 1
	for i := 0; i < L; i++ {
		color[i] = make([]int, H)
		for j := 0; j < H; j++ {
			color[i][j] = 0
		}
	}

	for i := 0; i < L; i++ {
		for j := 0; j < H; j++ {
			if string(S[i][j]) != "#" {
				continue
			}
			if color[i][j] != 0 {
				continue
			}
			maxc++
			color = dfs(S, i, j, maxc, color)
		}
	}
	return color
}

func main() {
	var H, W int
	fmt.Scan(&H, &W)
	S := make([]string, H)
	for i := 0; i < H; i++ {
		var s1 string
		fmt.Scan(&s1)
		S[i] = s1
	}
	col := multree(S)
	var ans map[int]int = map[int]int{}
	for i := 0; i < H; i++ {
		for j := range col[i] {
			if col[i][j] != 0 {
				ans[col[i][j]] = 1
			}
		}
	}
	fmt.Println(len(ans))
}
