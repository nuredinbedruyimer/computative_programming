class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left=0
        ans=1
        counter=0
        for right in range(len(nums)):
            
            while nums[right] *(right-left)-counter>k:
                counter-=nums[left]
                left+=1
            counter+=nums[right]
            ans=max(ans,right-left+1)
            
        return ans
