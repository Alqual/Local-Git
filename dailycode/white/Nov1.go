package main

import "math"

func minvector(ax []float64, ay []float64) (float64, int) {
	min := math.Sqrt((ax[0]-ax[1])*(ax[0]-ax[1]) + (ay[0]-ay[1])*(ay[0]-ay[1]))
	min2 := 0
	for i := 0; i < len(ax); i++ {
		for j := 0; (j < len(ay)) && (i != j); j++ {
			if math.Sqrt((ax[i]-ax[j])*(ax[i]-ax[j])+(ay[i]-ay[j])*(ay[i]-ay[j])) < min {
				min = math.Sqrt((ax[i]-ax[j])*(ax[i]-ax[j]) + (ay[i]-ay[j])*(ay[i]-ay[j]))
				min2 = i
			}
		}
	}
	return min, min2 + 1
}
