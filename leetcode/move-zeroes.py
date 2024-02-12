class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        def move_zeros():
            left=0
            for right in range(len(nums)):
                if nums[right]:
                    nums[left],nums[right]=nums[right],nums[left]
                    left+=1
            return nums
        return move_zeros()
        
     
         