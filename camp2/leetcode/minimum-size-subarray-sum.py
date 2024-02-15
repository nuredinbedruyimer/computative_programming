class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        [2,3,1,2,4,3]
        """
        what i neeed is finding sub arra with sum equal to target but with smalle
        number of size 
        first generete all subarray and  find weather the sub array equal the target
        and take the minimum of them
        using sliding window + prefix_sum 


        [1,2,2,3,3,4]
        using sliding window 
        """
        def get_answer():
            
            
            N = len(nums)
            curr_sum = 0
            min_window = N+1
            left = 0
            right =0
            while right<N:
                curr_sum+=nums[right]
                while curr_sum>=target:
                    curr_sum-=nums[left]
                    min_window = min(min_window, right-left+1)
                    left+=1
                right+=1
            return min_window if min_window !=N+1 else 0
        return get_answer()


       



            
            

        




        