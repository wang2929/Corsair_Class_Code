class Solution:
    def isValidSudoku(self, board) -> bool:
        row_tracker = [set() for _ in range(len(board))]
        col_tracker = [set() for _ in range(len(board))]
        box_tracker = [set() for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board)):
                elem = board[i][j]
                if elem.isdigit():
                    # row check
                    if elem not in row_tracker[i]:
                        row_tracker[i].add(elem)
                    else:
                        return False
                    # col check
                    if elem not in col_tracker[j]:
                        col_tracker[j].add(elem)
                    else:
                        return False
                    # box check
                    box_idx = ((i // 3) * 3) + (j // 3)
                    if elem not in box_tracker[box_idx]:
                        box_tracker[box_idx].add(elem)
                    else:
                        return False
        return True
    
board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
print(Solution().isValidSudoku(board))