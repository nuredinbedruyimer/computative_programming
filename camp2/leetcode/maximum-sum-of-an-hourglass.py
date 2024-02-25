class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        def get_answer():
            N = len(grid)
            M = len(grid[0])
            ans= 0
            for row in range(N-2):
               
                for column in range(1,M-1):
                    curr_sum = sum(grid[row][column-1:column+2])
                    middle = grid[row+1][column]
                    curr_sum_2 =sum(grid[row+2][column-1:column+2])
                    ans = max(curr_sum_2+curr_sum+middle, ans)
                    
            return ans
        return get_answer()



        