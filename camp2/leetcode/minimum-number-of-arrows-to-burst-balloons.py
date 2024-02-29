def get_answer(points):

    points.sort()
    prev_end = points[0][1]
    ans = 1

    for start, end in points[1:]:
        if start <= prev_end:
            prev_end = min(end, prev_end)
        else:
            ans += 1
            prev_end = end

    return ans


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        return get_answer(points)
