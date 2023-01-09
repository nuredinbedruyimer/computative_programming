class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxPairSum=0
        start=0
        end=len(nums)-1
        while start <end:
            maxPairSum=max(maxPairSum,nums[start]+nums[end])
            start=start+1
            end=end-1
        return maxPairSum