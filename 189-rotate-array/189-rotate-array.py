class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)
        left=0
        right=len(nums)-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left=left+1
            right=right-1
        print(nums)
        left=0
        right=k-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left=left+1
            right=right-1
        print(nums)
        left=k
        right=len(nums)-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left=left+1
            right=right-1
        print(nums)
            
        
        
     