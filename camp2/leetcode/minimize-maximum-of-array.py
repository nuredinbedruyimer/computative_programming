class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def get_answer():

            max_value = 0
            curr_sum = 0
            N = len(nums)

            for i in range(N):
                curr_sum += nums[i]
                middle = math.ceil(curr_sum / (i + 1))
                max_value = max(max_value, middle)

            return max_value
        return get_answer()
