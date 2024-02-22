class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        """

        """
        1 2 3 ----swap the row    7 8 9 ---->then do transponse of it 7 4 1 
        4 5 6                     4 5 6                               8 5 2
        7 8 9                     1 2 3                               9 6 3

        if n is odd no need to swap the last row then using unmeeted pointer
        
        """
        def swap(N):
            left = 0
            right = N-1
            while left<right:
                matrix[left], matrix[right] = matrix[right], matrix[left]
                left+=1
                right-=1
            
        def get_answer():
            N = len(matrix)
            M = len(matrix[0])
            # reverse the matrix in row
            swap(N)
           
            for row in range(N):
                for column in range(row):
                    #  swapping
                    matrix [row][column],matrix[column][row]=matrix[column][row], matrix [row][column]
        get_answer()
        

        