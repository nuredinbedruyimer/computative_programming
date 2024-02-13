class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        def get_answer():
            zero = 0
            one = nums.count(1)
            N = len(nums)
            memo = [0 for _ in range(N+1)]
            
            for i in range(N):
                
                memo[i] = zero +one
                if nums[i] ==0:
                    zero+=1
                else:
                    one-=1
            memo[-1] = zero
            max_value = max(memo)
            ans = []
            for i in range(len(memo)):
                if memo[i]==max_value:
                    ans.append(i)
            return  ans
        return get_answer()
                


        