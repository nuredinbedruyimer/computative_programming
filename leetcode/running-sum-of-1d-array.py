class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        def get_answer():
            N = len(nums)
            ans = [nums[0]]
            for i in range(1,N):
                ans.append(ans[-1]+nums[i])
            return ans
        return get_answer()