class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        length=len(nums)
        heap=[(-nums[0],0)]
        for i in range(1,length):
            while heap[0][1]<i-k:
                heapq.heappop(heap)
            maxValue=heap[0][0]
            heapq.heappush(heap,(maxValue-nums[i],i))
            if i==length-1:
                return -(maxValue-nums[i])
        return nums[0]
        