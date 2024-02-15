class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer=0
        for right in range(len(nums)):
            if nums[right]!=val:
                nums[pointer]=nums[right]
                pointer=pointer+1
            print(nums)
        
                
                
                
            
        return pointer
        
        