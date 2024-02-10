class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        def get_answer():
            N = len(nums)
            prefix_sum=[0 for _ in range(len(nums))]
            prefix_sum[0]=nums[0]
            for i in range(1,N):
                prefix_sum[i]=prefix_sum[i-1]+nums[i]
            suffix_sum=[0 for _ in range(len(nums))]
            suffix_sum[len(nums)-1]=nums[len(nums)-1]
            for i in range(N-2,-1,-1):
                suffix_sum[i]=suffix_sum[i+1]+nums[i]
            ans = []

            for i in range(N):
                left = i+1
                current_one = nums[i]*left-prefix_sum[i]
                right = N-i
                current_two = suffix_sum[i]-nums[i]*right
                ans.append(current_one + current_two)

            return  ans
        return get_answer()