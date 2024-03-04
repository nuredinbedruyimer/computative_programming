class Solution(object):
    def triangleNumber(self, nums):
        nums.sort()
        counter=0
        for start in range(2,len(nums)):
            left=0
            right=start-1
            while left<right:
                if nums[left]+nums[right]>nums[start]:
                    counter+=(right-left)
                    right=right-1
                else:
                    left=left+1
        return counter
                
                
            
                
                
        
        
        