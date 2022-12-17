class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)
        n=len(nums)-k
        while(n!=0):
            heappop(nums)
            n=n-1
        return nums[n]
        