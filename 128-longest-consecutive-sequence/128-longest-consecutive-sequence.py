class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        length=0
        for currentValue in nums:
            if currentValue-1 not  in nums:
                start=currentValue
                while start in nums:
                    start=start+1
                    
                length=max(length,start-currentValue)
        return length
        