def get_answer(grid):

    N = len(grid)

    rows =  [0 for _ in range(N)]

    columns = [ 0 for _ in range(N)]

    ans = 0

    for row in range(N):

        for column in range(N):

            rows[row] = max(rows[row], grid[row][column])

            columns[column] = max(columns[column] , grid[row][column])

    for row in range(N):
        for column in range(N):
            min_value = min(rows[row], columns[column])

            ans += max(min_value-grid[row][column], 0)

    return ans






class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:

        return get_answer(grid)
        