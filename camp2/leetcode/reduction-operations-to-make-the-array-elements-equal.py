class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        def get_answer():
            N= len(nums)
            nums.sort()
            ans = 0
            for i in range(N-2, -1, -1):
                if nums[i]!=nums[i+1]:
                    ans+=N-i-1
                else:
                    continue
            return ans
        return get_answer()

        