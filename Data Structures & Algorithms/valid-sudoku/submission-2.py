class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for ind in range(9):
                if board[row][ind] == ".":
                    continue
                if board[row][ind] in seen:
                    return False
                seen.add(board[row][ind])
        for col in range(9):
            seen = set()
            for ind in range(9):
                if board[ind][col] == ".":
                    continue
                if board[ind][col] in seen:
                    return False
                seen.add(board[ind][col])
        for box in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (box // 3) * 3 + i
                    col = (box % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True
