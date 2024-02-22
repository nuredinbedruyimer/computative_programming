class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        def next_greater_stack(arr):
            stack = []
            ans = [-1] * len(arr)
            for i in range(2):
                for current_index, current_value in enumerate(arr):
                    while stack and stack[-1][1] < arr[current_index]:
                        _index, _value = stack.pop()
                        ans[_index] = current_value

                    stack.append([current_index, current_value])

            return ans

        return next_greater_stack(nums)
