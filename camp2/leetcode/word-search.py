def search_word(board, word, row, column, current_word, m, n, seen):

    if len(word) == current_word:

        return True
    a = row < 0 or column < 0 or row >= m or column >= n
    b =  word[current_word] != board[row][column] or (row , column)  in seen if not a else False

    if  a or b :
        return False
    seen.add((row, column))
    #  move down 

    down = search_word (board,word, row + 1, column , current_word + 1, m, n,seen)

    #  move up 

    up = search_word (board, word, row - 1,column , current_word + 1, m, n, seen)

    # move right

    right  = search_word (board,word, row, column + 1 , current_word + 1, m, n, seen)

    # move left

    left  = search_word (board, word, row, column - 1 , current_word + 1, m, n, seen)

    seen.remove((row, column))
    return  down or up or right or left



    



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        seen = set()
        for r in range(m):
            for c in range(n):
                if search_word(board, word, r, c,0,m, n, seen):
                    return True
        return False
        