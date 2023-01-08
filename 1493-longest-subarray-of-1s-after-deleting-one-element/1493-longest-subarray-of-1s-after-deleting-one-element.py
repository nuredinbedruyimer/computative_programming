class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums)==nums.count(1):
            return len(nums)-1
        firstCounter=0
        secondCounter=0
        maxCounter=0
        for i in range(len(nums)-1):
            if nums[i]==1:
                firstCounter+=1
            else:
                for j in range(i+1,len(nums)):
                    if nums[j]==0:
                        break
                    else:
                        secondCounter+=1
                if maxCounter<(firstCounter+secondCounter):
                    maxCounter=firstCounter+secondCounter
                firstCounter=0
                secondCounter=0
        return maxCounter
        