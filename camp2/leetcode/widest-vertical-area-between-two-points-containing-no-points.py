class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        def get_answer():
            points.sort()
            N = len(points)
            ans = 0
            for i in range(N-1):
                ans = max(ans, points[i+1][0]-points[i][0])
            return ans
        return get_answer()
                
        