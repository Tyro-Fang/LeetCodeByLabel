type IntHeap [][2]int

func (h IntHeap) Less(i, j int) bool     { return h[i][1] < h[j][1] }
func (h IntHeap) Swap(i, j int)   { h[i], h[j] = h[j], h[i] }
func (h IntHeap) Len() int      { return len(h)}

func (h *IntHeap) Push(x interface{}) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.([2]int))
}

func(h *IntHeap)Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n - 1]
    *h = old[0: n - 1]
    return x
}


func topKFrequent(nums []int, k int) []int {
    dict := make(map[int]int)
    for _,v := range nums{
        dict[v] ++
    }

    h := &IntHeap{}
    heap.Init(h)
    
    for key, val := range dict{
        heap.Push(h, [2]int{key, val})
        if h.Len() > k {
            heap.Pop(h)
        }
    }

    


    res := make([]int, k)
    for i := 0;i < k; i++ {
        res[i] = heap.Pop(h).([2]int)[0]
    }
    return res
}