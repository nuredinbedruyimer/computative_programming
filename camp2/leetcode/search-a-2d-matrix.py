class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        column = len(matrix[0])
        low = 0
        high = row * column
        while low < high:

            middle = ( low + high ) // 2

            curr_row = middle // column

            curr_col = middle % column
            if curr_row >= row or curr_col >= column:

                continue

            elif matrix[curr_row][curr_col] > target:

                high -= 1

            elif matrix[curr_row][curr_col] < target:

                low += 1

            else:

                return  True
                
        return False

        