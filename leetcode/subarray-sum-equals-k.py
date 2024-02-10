class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        def get_answer():
            curr_sum = 0
            memo ={0:1}
            N = len(nums)
            ans = 0
            for i in range(N):
                curr_sum+=nums[i]
                compliment = curr_sum - k
                if compliment in memo:
                    ans+=memo[compliment]
                if curr_sum in memo:
                    memo[curr_sum]+= 1
                else:
                    memo[curr_sum]=1
                
                
            return ans
        return get_answer()

    
            
        