class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # for case of all one's
        if len(nums)==nums.count(1):
            return len(nums)-1
       
        firstCounter=0
        secondCounter=0
        maxCounter=0
        stack=[]
        # nums with atleast one zero
        for left in range(len(nums)):
            if nums[left]==1:
                firstCounter+=1
                
            else:
                for right in range(left+1,len(nums)):
                    if nums[right]==0:
                        break
                    else:
                        secondCounter+=1
                       
                if maxCounter<(firstCounter+secondCounter):
                    maxCounter=firstCounter+secondCounter
                firstCounter=0
                secondCounter=0
        return maxCounter
        