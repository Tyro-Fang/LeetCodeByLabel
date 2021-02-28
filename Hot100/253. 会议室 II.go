type IntHeap []int
func (h IntHeap) Len() int{
    return len(h)
}
func(h IntHeap) Less(i, j int) bool {
    return h[i] < h[j]
}
func(h IntHeap) Swap(i, j int){
    h[i], h[j] = h[j], h[i]
}
func(h *IntHeap) Push(x interface{}){
    *h = append(*h, x.(int))
}
func(h *IntHeap) Pop() interface{}{
    old := *h
    n := len(old)
    x := old[n - 1]
    *h = old[:n - 1]
    return x
}
func Max(a, b int) int {
    if a < b {
        return b
    }
    return a
}

func minMeetingRooms(intervals [][]int) int {
    sort.Slice(intervals, func(i, j int)bool{
        return intervals[i][0] < intervals[j][0]
    })
    h := &IntHeap{}
    heap.Init(h)
    res := 0
    for i := 0; i < len(intervals); i++ {
        for ;len(*h) != 0 && intervals[i][0] >= (*h)[0];{
            heap.Pop(h)
        }
        heap.Push(h, intervals[i][1])
        res = Max(res, len(*h))
    }
    return res
}
