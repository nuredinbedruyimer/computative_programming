class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        def get_answer():
            m = len(matrix[0])
            n = len(matrix)
            ans = [[-1 for _ in range(n)] for _ in  range(m)]
            
            for row in range(n):
                
                for column in range(m):
                    ans[column][row] = matrix[row][column]
            return ans

                    
        return get_answer()
        