package main
import "fmt"

var sc = bufio.NewScanner(os.Stdin)
var buffer = make([]byte, 10000)

func Newline() []int {
	sc.Scan()
	arr := strings.Split(sc.Text(), " ")
	ret := make([]int, len(arr))
	for i, v := range arr {
		ret[i], _ = strconv.Atoi(v)
	}
	return ret
}

func main(){
	W := Newline()
	W[1]--
	W[2]--
	dist:= make([][]int, W[0])
	for i := 0; i < W[0]; i++ {
		for j := 0; j < W[0]; j++ {
		dist[i][j] = -1
	}
	for k := 0; k < W[0]; k++ {
		var queue []int
		queue = append(queue, k)
		dist[k][k] = 0
		while len(queue) > 0 {
			
	}
	


}