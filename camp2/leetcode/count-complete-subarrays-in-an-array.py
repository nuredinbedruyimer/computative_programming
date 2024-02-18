class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        def get_answer():
            N = len(nums)
            window = len(set(nums))
            left = 0
            ans = 0
            memo ={}
            for right in range(N):
                memo[nums[right]] = 1+memo.get(nums[right], 0)
                while left<N and len(memo)==window:
                    ans+=N-right
                    memo[nums[left]]-=1
                    if memo[nums[left]]==0:
                        del memo[nums[left]] 
                    left+=1
            return ans
        return get_answer()

        