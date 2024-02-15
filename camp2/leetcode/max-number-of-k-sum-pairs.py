class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        def get_answer():
            nums.sort()
            left = 0
            right = len(nums)-1
            opt = 0
            while left<right:
                curr_sum  = nums[right] + nums[left]

                if curr_sum>k:

                    right -=1
                elif curr_sum < k:
                    
                    left+=1
                else:
                    opt+=1
                    right-=1
                    left+=1
            return opt
        return get_answer()

        