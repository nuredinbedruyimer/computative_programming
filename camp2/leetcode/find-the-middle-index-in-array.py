class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
       



        def get_answer():
            prefix_sum= [nums[0]]
            N = len(nums)

            for i in range(1,N):
                prefix_sum.append(prefix_sum[-1]+nums[i])
            suffix_sum = [nums[-1]]
            for i in range(N-2, -1, -1):
                suffix_sum.append(suffix_sum[-1]+nums[i])
            for i in range(N):
                if prefix_sum[i]==suffix_sum[N-i-1]:
                    return i
            return -1
        return get_answer()

        