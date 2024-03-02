def is_good_position(board, row, column, n):
        r = row
        c = column


        while row >= 0 and column >= 0:
            if board[row][column] == 'Q':
                return False
            row -= 1
            column -= 1


        column = c
        row = r
        while column >= 0:
            if board[row][column] == 'Q':
                return False
            column -= 1


        row = r
        column = c
        while row < n and column >= 0:
            if board[row][column] == 'Q':
                return False
            row += 1
            column -= 1


        return True


def n_queen_solve(col, board, ans, n):
    if col == n:
        ans.append(list(board))
        return


    for row in range(n):
        if is_good_position(board,row, col, n):
            board[row] = board[row][:col] + 'Q' + board[row][col+1:]
            n_queen_solve(col+1, board, ans, n)
            board[row] = board[row][:col] + '.' + board[row][col+1:]







class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        ans = []
        board = ['.'*n for _ in range(n)]
        n_queen_solve(0, board, ans, n)
        return ans