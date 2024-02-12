class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        def get_answer():
           
        
            
            ans = []
            memo = {}
            N = len(nums)
            arr = nums[:]
            nums.sort()
            
            for i in range(N):
                if nums[i] not in memo:
                    memo[nums[i]] = i
            
            for num in arr:
                ans.append(memo[num])
            
            return ans
        return get_answer()


        
        