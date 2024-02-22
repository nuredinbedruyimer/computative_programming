class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        def get_answer():
            N = len(mat)
            ans = 0
            for row in range(N):
                ans +=mat[row][row] + mat[row][-row-1]
            if  N%2==0:
                return ans
            else:
                ans = ans-mat[N//2][N//2]
                return ans 
        return get_answer()
        