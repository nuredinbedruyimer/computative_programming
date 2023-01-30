class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left=0
    
        maxOne=0
        for right in range(len(nums)):
            if nums[right]==0:
                right=right+1
                left=right
            else:
                right=right+1
            maxOne=max(right-left,maxOne)
        return maxOne
       
                
            
        