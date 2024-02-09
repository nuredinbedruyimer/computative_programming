class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """
        [4,5,0,-2,-3,1] k =5

        curr_sum = 9
        memo ={0:1, 4:1,}
        do the thing come on
        
        
        """
        def get_answer():
            curr_sum= 0
            N = len(nums)
            ans = 0
            memo = {0:1}
            for i in range(N):
                curr_sum+=nums[i]
                if curr_sum%k in memo:
                    ans+=memo[curr_sum%k]
                if curr_sum%k in memo:
                    memo[curr_sum%k]+=1
                else:
                    memo[curr_sum%k]=1
            return ans
        return get_answer()

        