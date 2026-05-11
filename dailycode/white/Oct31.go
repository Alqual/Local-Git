package main
import "fmt","math"

func tetra(x []int, y []int, z []int) int { //３つの座標配列から四面体を構成する組を返す関数
	var Ret_x, Ret_y, Ret_z []int := []int{}, []int{}, []int{}
	for i := 0; i < len(x); i++ {
		for j := 0; j < len(y); j++ {
			for k := 0; k < len(z); k++ {
				if abs(sqrt(abs((x[i]-x[j])**2 + (y[i]-y[j])**2 + (z[i]-z[j])**2)) - sqrt(abs((x[i]-x[k])**2 + (y[i]-y[k])**2 + (z[i]-z[k])**2))) <\
				 sqrt(abs((x[i]-x[j])**2 + (y[i]-y[j])**2 + (z[i]-z[j])**2))<\
				  abs(sqrt(abs((x[i]-x[j])**2 + (y[i]-y[j])**2 + (z[i]-z[j])**2)) + sqrt(abs((x[i]-x[k])**2 + (y[i]-y[k])**2 + (z[i]-z[k])**2)) ){
					
				{}
			}
		}
	}

}