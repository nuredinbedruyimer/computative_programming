class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_sum = 0
        """
         -1  2  1  -4 
         after sorting
         -4 -1  1  2
             i  L   R
        
        """
        def get_answer():
            nums.sort()
            difference = float('inf')
            closest = 0
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                left = i+1
                right = len(nums)-1
                while left < right:
                    sum_so_far = nums[i] + nums[left]+nums[right]
                    difference_here = abs(sum_so_far-target)
                    if difference_here < difference:
                        closest= sum_so_far
                        difference = difference_here
                    
                    if sum_so_far >= target:
                        right = right -1
                    else:
                        left = left + 1
            return closest
        return get_answer()
       


        