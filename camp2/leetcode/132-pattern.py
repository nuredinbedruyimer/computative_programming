class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        def find_123():
            stack = []
            _min = nums[0]

            for curr in nums[1:]:
                while stack and curr >= stack[-1][0]:
                    stack.pop()
                #  because there are duplicate element
                if stack and curr > stack[-1][1]:
                    return True

                stack.append([curr, _min])
                _min = min(_min, curr)

            return False
        return find_123()

        