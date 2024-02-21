class Solution:
    def trap(self, height: List[int]) -> int:
        """     |
        |     | |  |
        | |   | |  |
        | | | | |  |
          L        R
        """
        def get_answer():
            N = len(height)
            left = 0
            right = N-1
            area =  0
            left_maximum = height[left]
            right_maximum = height[right]
            while left<right:
                # case one if left height is greater than right then keep it and move 
                if height[left]>=height[right]:
                    if height[right]>right_maximum:
                        right_maximum = height[right]
                    else:
                        area += right_maximum - height[right]
                    right-=1
                else:
                    # when we get greater height keep it as new max left height else calculete the area
                    if height[left]>left_maximum:
                        left_maximum = height[left]
                    else:
                        area+=left_maximum-height[left]
                    left+=1
            return area
        return get_answer()

