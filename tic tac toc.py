import random
import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.buttons = self.create_buttons()

    def create_buttons(self):
        buttons = []
        for i in range(9):
            button = tk.Button(self.root, text=" ", font=('normal', 40), width=5, height=2,
                               command=lambda i=i: self.player_move(i))
            button.grid(row=i//3, column=i%3)
            buttons.append(button)
        return buttons

    def player_move(self, i):
        if self.board[i] == " ":
            self.board[i] = self.current_player
            self.buttons[i].config(text=self.current_player)
            if self.check_winner(self.current_player):
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.is_full():
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O"
                self.root.after(500, self.computer_move)

    def computer_move(self):
        empty_cells = [i for i in range(9) if self.board[i] == " "]
        move = random.choice(empty_cells)
        self.board[move] = self.current_player
        self.buttons[move].config(text=self.current_player)
        if self.check_winner(self.current_player):
            messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
            self.reset_game()
        elif self.is_full():
            messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            self.reset_game()
        else:
            self.current_player = "X"

    def check_winner(self, player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        return any(all(self.board[cell] == player for cell in condition) for condition in win_conditions)

    def is_full(self):
        return all(cell != " " for cell in self.board)

    def reset_game(self):
        self.board = [" " for _ in range(9)]
        for button in self.buttons:
            button.config(text=" ")
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game= TicTacToe(root)
    root.mainloop()
