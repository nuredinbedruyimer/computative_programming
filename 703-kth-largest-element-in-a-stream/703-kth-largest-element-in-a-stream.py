import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap=nums
        self.k=k
        heapify(self.minHeap)
        while(len(self.minHeap)>self.k):
            heappop(self.minHeap)
        
        

    def add(self, val: int) -> int:
        self.val=val
        heappush(self.minHeap,self.val)
        if(len(self.minHeap)>self.k):
            heappop(self.minHeap)
        return self.minHeap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)