package main

import "container/heap"

// IntHeapの実装
type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

// 実際の処理
//func main() {
//	ih := &IntHeap{}
//	heap.Init(ih)
//	for i := 0; i < 1e7; i++ {
//		// データのPush
//		// 性能を見るために、1e4で割った余りをPushしている
//		heap.Push(ih, i%1e4)
//	}
//	for i := 0; i < 1e7; i++ {
//		// データのPop
//		_ = heap.Pop(ih)
//	}
//}
// AtCoderでの実行速度
// 実行時間 3993ms
// メモリ 405380KB

//priority queue

type Edge struct {
	To     int // 移動先のNode
	Weight int // コスト
}
type EdgeHeap []Edge

func (h EdgeHeap) Len() int           { return len(h) }
func (h EdgeHeap) Less(i, j int) bool { return h[i].Weight < h[j].Weight }
func (h EdgeHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *EdgeHeap) Push(x interface{}) {
	*h = append(*h, x.(Edge))
}

func (h *EdgeHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

const c1 = 1<<20 - 1
const c2 = 1<<6 - 1

func main() {
	eh := &EdgeHeap{}
	heap.Init(eh)
	for i := 0; i < c1; i++ {
		// データのPush
		// 性能を見るために、1e4で割った余りをPushしている
		heap.Push(eh, Edge{To: i, Weight: i % c2})
	}
	for i := 0; i < c1; i++ {
		// データのPop
		_ = heap.Pop(eh).(Edge)
	}
}

// AtCoderでの実行速度
// 実行時間 4695ms
// メモリ 658724KB
