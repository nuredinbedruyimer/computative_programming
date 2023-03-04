import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def helper(nums,target):
            left=0
            right=len(nums)-1
            while left<=right:
                middle=(left+right)//2
                if target>nums[middle]:
                    left=middle+1
                if target<nums[middle]:
                    right=middle-1
                if target==nums[middle]:
                    return True
            return False
        print(helper(nums,target))
        if helper(nums,target) and len(nums)>1:
            valueOne=bisect.bisect_left(nums,target)
            print(valueOne)
            valueTwo=bisect.bisect_right(nums,target)
            return [valueOne,valueTwo-1]
        elif len(nums)==1 and helper(nums,target):
            return [0,0]
        else:
            return[-1,-1]
        
        
        
        
        
        