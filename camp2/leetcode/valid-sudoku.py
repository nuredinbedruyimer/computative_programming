class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        check row wise and check column wise 
        row ---> some ditectng method set 
        column --- column as key set as value 
        and check the box of 3 X 3  using also by using set represent that by some in
        dex like thing

        """
        def get_answer():
            # using this variable instead of constant or literal value it increase reuseablity
            soduku_size = 9
            box_size = 3
            box = defaultdict(set)
            rows = defaultdict(set)
            columns = defaultdict(set)
            #  we divide by 3 the index for box to make use it it track every box using some fixed box
            for row in range(soduku_size):
                for column in range(soduku_size):
                    # check current element is valid candidate for valid sodulu
                    if (board[row][column] in rows[row]) or (board[row][column] in  box[(row//box_size,column//box_size)])or (board[row][column] in columns[column]):
                        return False
                    if board[row][column]=='.':
                        continue
                    box[(row//box_size,column//box_size)].add(board[row][column])
                    rows[row].add(board[row][column])
                    columns[column].add(board[row][column])
            return True
        return get_answer()


        