class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows,cols=len(matrix),len(matrix[0])
        self.sumMath=[[0]*(cols+1) for right in range(rows+1)]
        for right in range(rows):
            prefix=0
            for counter in range(cols):
                prefix+=matrix[right][counter]
                above=self.sumMath[right][counter+1]
                self.sumMath[right+1][counter+1]=prefix+above
                
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1=row1+1
        row2=row2+1
        col1=col1+1
        col2=col2+1
        bottomRight=self.sumMath[row2][col2]
        above=self.sumMath[row1-1][col2]
        left=self.sumMath[row2][col1-1]
        topLeft=self.sumMath[row1-1][col1-1]
        return bottomRight+topLeft-above-left
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)