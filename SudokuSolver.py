class Sudoku:
    def __init__(self, board):
        assert len(board) == 9, "Invalid board"
        for i in board:
            assert len(i) == 9, "Invalid board"
        self.board = board
        self.unfilled = [(r, c) for r in range(9) for c in range(9) if self.board[r][c] == 0]

    def isValid(self, r, c, num):
        for i in range(9):
            if self.board[r][i] == num and i != c:
                return False
        for i in range(9):
            if self.board[i][c] == num and i != r:
                return False
        r_corner, c_corner = r - (r % 3), c - (c % 3)
        for tR in range(r_corner, r_corner + 3):
            for tC in range(c_corner, c_corner + 3):
                if self.board[tR][tC] == num and (r, c) != (tR, tC):
                    return False
        return True

    def solve(self):
        assert self._solve(0), "Impossible board"

    def _solve(self, idx):
        if idx >= len(self.unfilled):
            return True
        r, c = self.unfilled[idx]
        for num in range(1, 10):
            self.board[r][c] = num
            if not self.isValid(r, c, num): continue
            if self._solve(idx+1):
                return True
        self.board[r][c] = 0
        return False

    def print(self):
        for row in self.board:
            print(*row)

if __name__ == "__main__":
    import SudokuSolver_Checker
    SudokuSolver_Checker.validate()