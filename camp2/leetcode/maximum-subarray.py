class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        ucsing kadanes rule and prefix sum 
        whenever we have curr_sum<0 make it zero and do our actio

        
        
        """
        def get_answer():
            curr_sum  = 0
            N = len(nums)
            max_sum = nums[0]
            for i in range(N):
                curr_sum+=nums[i]
                max_sum = max(max_sum, curr_sum)
                curr_sum = max(curr_sum, 0)

            return max_sum
        return get_answer()


        