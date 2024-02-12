class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        def remove_depulicate(nums):
                    left = 0
                    N = len(nums)
                    counter =1
                    for right in range(N):
                        if nums[right] !=nums[left]:
                            left = left+1
                            nums[right],nums[left ] = nums[left ],nums[right]
                            
                            counter +=1
                    return counter 
        return remove_depulicate(nums)
        