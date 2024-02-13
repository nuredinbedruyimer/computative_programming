class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        # -7 -6 -2 -1 2 3 5
        left=0
        right=len(nums)-1
        counter=0
        
        while left<right:
            currSum=nums[left]+nums[right]
            if currSum<target:
                counter+=right-left
                left=left+1
            else:
                right=right-1
        return counter
            
        