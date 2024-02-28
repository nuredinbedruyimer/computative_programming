class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        """
        3  9  3
         9 -->3 + 6
         6 ---> 2
           3 3 3 3  3
        
        
        """
        
        N = len(nums)
        ans = 0
        for i in range(N-2, -1, -1):
            if nums[i]>nums[i+1]:
                
                space =(nums[i+1]+nums[i]-1)//nums[i+1]
                ans+=space-1
                nums[i] = nums[i]//space
                
                
            else:
                continue
        return ans

        