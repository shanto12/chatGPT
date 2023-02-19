import tkinter as tk
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")

        self.current_player = "X"
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

        self.buttons = [[tk.Button(master, text=" ", font=("Arial", 30), height=2, width=5, command=lambda row=i, col=j: self.make_move(row, col)) for j in range(3)] for i in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].grid(row=i, column=j)

        self.label = tk.Label(master, text="Player " + self.current_player + "'s turn", font=("Arial", 16))
        self.label.grid(row=3, columnspan=3)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_win():
                self.label.config(text="Player " + self.current_player + " wins!")
                for i in range(3):
                    for j in range(3):
                        self.buttons[i][j].config(state=tk.DISABLED)
            elif self.check_draw():
                self.label.config(text="It's a draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.label.config(text="Player " + self.current_player + "'s turn")
                if self.current_player == "O":
                    self.computer_move()
        else:
            self.label.config(text="That space is already taken. Try again.")

    def computer_move(self):
        row, col = self.get_best_move()
        self.board[row][col] = "O"
        self.buttons[row][col].config(text="O")
        if self.check_win():
            self.label.config(text="Computer wins!")
            for i in range(3):
                for j in range(3):
                    self.buttons[i][j].config(state=tk.DISABLED)
        elif self.check_draw():
            self.label.config(text="It's a draw!")
        else:
            self.current_player = "X"
            self.label.config(text="Player X's turn")

    def get_best_move(self):
        # Use a simple strategy to find the best move: choose a random empty cell
        empty_cells = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    empty_cells.append((i, j))
        return random.choice(empty_cells)

    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        return False

    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    return False
        return True

root = tk.Tk()
tictactoe = TicTacToe(root)
root.mainloop()
