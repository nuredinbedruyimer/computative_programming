class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        def get_answer():
            memo = defaultdict(list)
            N = len(nums)
            ans = [0 for i in range(N)]
            for i in range(N):
                memo[nums[i]].append(i)
            for value, indexes in memo.items():
                length = len(indexes)

                suffix_sum = sum(indexes)
                prefix_sum = 0
                for i in range(length):
                    curr = memo[value][i]
                    ans[curr] = (i * curr - prefix_sum) + (
                        suffix_sum - curr - (length - 1 - i) * curr
                    )
                    suffix_sum -= curr
                    prefix_sum += curr
            return ans

        return get_answer()
