import tkinter as tk
from tkinter import messagebox

# Check if it's safe to place a number in a given position
def is_safe(board, row, col, num):
    for i in range(9):
        if board[row][i] == num:
            return False
        if board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

# Backtracking algorithm function
def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_safe(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# Extract Sudoku input
def get_board():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            value = entry_widgets[i][j].get()
            row.append(int(value) if value != "" else 0)
        board.append(row)
    return board

# Display the solved Sudoku
def update_sudoku(board):
    for i in range(9):
        for j in range(9):
            entry_widgets[i][j].delete(0, tk.END)
            entry_widgets[i][j].insert(0, str(board[i][j]))

# Handle the solve button click
def solve_button_click():
    board = get_board()
    if solve_sudoku(board):
        update_sudoku(board)
    else:
        messagebox.showinfo("No Solution", "No solution exists for the given Sudoku puzzle.")

# Create the main tkinter window
root = tk.Tk()
root.title("Sudoku Solver")

# Create the grid of entry widgets for input
entry_widgets = []
for i in range(9):
    row_entries = []
    for j in range(9):
        entry = tk.Entry(root, width=3, font=("Arial", 18), justify="center")
        entry.grid(row=i, column=j, padx=5, pady=5)
        row_entries.append(entry)
    entry_widgets.append(row_entries)

# Create the Solve button
solve_button = tk.Button(root, text="Solve", font=("Arial", 14), command=solve_button_click)
solve_button.grid(row=9, column=0, columnspan=9, pady=10)

root.mainloop()
