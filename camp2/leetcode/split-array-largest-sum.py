class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        """
        prefix_sum_to count sub arrray with sum of  k
        finding o value for
        LOW =max(value_of_array)
        HIGH = sum(value_of_array)


        """

        def black_box(target):
            counter = 1
            curr_sum = 0
            for i in range(len(nums)):
                curr_sum += nums[i]
                if curr_sum > target:
                    counter += 1
                    curr_sum = nums[i]
            return counter <= k

        def get_answer():
            low = max(nums)
            high = sum(nums)
            ans = low
            while low <= high:
                target = (low + high) // 2
                if black_box(target):
                    ans = target
                    high = target - 1
                else:
                    low = target + 1
            return ans

        return get_answer()
