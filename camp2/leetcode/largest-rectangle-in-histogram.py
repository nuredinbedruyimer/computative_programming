class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def max_histogram(arr):
            length = len(arr)
            stack = []
            area = 0

            for curr_index in range(length+1):
                while stack and (curr_index == length or stack[-1][1] > arr[curr_index]):
                    _, height = stack.pop()

                    if not stack:
                        width = curr_index
                    else:
                        width = curr_index - stack[-1][0]-1
                    area = max(width * height, area)

                if curr_index < length:
                    stack.append((curr_index, arr[curr_index]))
            return area
        return max_histogram(heights)
        