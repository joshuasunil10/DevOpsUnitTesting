def solve_sudoku(board):
    """Solves the Sudoku puzzle using backtracking.
    Args:
        board (list): A 9x9 list of lists representing the Sudoku board. Empty cells should be 0.
    Returns:
        list or None: The solved board as a list or None if unsolvable.
    """
    def is_valid_move(board, row, col, num):
        """Checks if placing num at (row, col) is valid."""
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        box_row_start, box_col_start = 3 * (row // 3), 3 * (col // 3)
        for r in range(box_row_start, box_row_start + 3):
            for c in range(box_col_start, box_col_start + 3):
                if board[r][c] == num:
                    return False
        return True

    def solve():
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid_move(board, row, col, num):
                            board[row][col] = num
                            if solve():
                                return True
                            board[row][col] = 0
                    return False
        return True

    if solve():
        return board
    return None
