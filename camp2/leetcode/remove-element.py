class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        def get_answer():
            left=0
            for right in range(len(nums)):
                if nums[right]!=val:
                    nums[left]=nums[right]
                    left=left+1
            return left
        return get_answer()
        
        