class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        tempSum=0
        ans=float('inf')
        for right in range(len(nums)):
            tempSum+=nums[right]
            while tempSum>=target:
                ans=min(ans,right-left+1)
                tempSum-=nums[left]
                left=left+1
        return 0 if ans==float('inf') else ans
                
                