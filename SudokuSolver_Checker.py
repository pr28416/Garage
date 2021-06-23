from SudokuSolver import Sudoku

def validate():
    with open("SudokuBoards.txt") as fin:
        with open("SudokuOutput.txt") as fout:
            for t in range(50):
                board = []

                for i in range(9):
                    board.append([int(j) for j in fin.readline().strip("\n")])

                sudoku = Sudoku(board)
                sudoku.solve()
                passed = True
                for i in range(9):
                    passed = passed and " ".join(map(str,sudoku.board[i])) == fout.readline().strip("\n")

                print(f"Test case {t+1}", "passed." if passed else "failed.")