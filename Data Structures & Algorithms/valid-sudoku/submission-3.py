class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, squares = defaultdict(set), defaultdict(set), defaultdict(set)
        # Squares keyed by (row // 3, ccol // 3)
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == ".":
                    continue
                val = board[row][col]
                if val in rows[row] or val in cols[col] or val in squares[(row // 3, col // 3)]:
                    return False
                else:
                    rows[row].add(val)
                    cols[col].add(val)
                    squares[(row // 3, col // 3)].add(val)
        
        return True