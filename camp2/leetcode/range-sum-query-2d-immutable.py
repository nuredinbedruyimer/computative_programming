class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows,columns=len(matrix),len(matrix[0])
        sum_matrix=[[0 for _ in range(columns+1)] for right in range(rows+1)]
        for row in range(rows):
            prefix=0
            for column in range(columns):
                prefix+=matrix[row][column]
                above=sum_matrix[row][column+1]
                sum_matrix[row+1][column+1]=prefix+above
        self.sum_matrix = sum_matrix
                
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1=row1+1
        row2=row2+1
        col1=col1+1
        col2=col2+1
        bottom_right=self.sum_matrix[row2][col2]
        above=self.sum_matrix[row1-1][col2]
        left=self.sum_matrix[row2][col1-1]
        top_left=self.sum_matrix[row1-1][col1-1]
        return bottom_right+top_left-above-left
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)