from tkinter import *
from tkinter import ttk
import tkinter.messagebox

root = Tk()
root.title("Tic Tac Toe")

# Global Variables
a = 1  # 1 for Player 1 (X), 0 for Player 2 (O)
b = 0  # Number of moves
c = 0  # 1 if the game ends, 0 otherwise

# Restart Game
def restartbutton():
    global a, b, c
    a = 1
    b = 0
    c = 0
    playerturn["text"] = "Player 1 Turn!"
    for button in buttons:
        button.config(text=" ", state=NORMAL)

# Disable Buttons
def disable_buttons():
    for button in buttons:
        button.config(state=DISABLED)

# Button Click Logic
def buttonclick(id):
    global a, b, c

    button = buttons[id - 1]

    if button["text"] == " " and c == 0:  # Only proceed if button is empty
        if a == 1:  # Player 1's Turn
            button["text"] = "X"
            playerturn["text"] = "Player 2 Turn!"
            a = 0
        else:  # Player 2's Turn
            button["text"] = "0"
            playerturn["text"] = "Player 1 Turn!"
            a = 1

        b += 1  # Increment moves
        check_winner()  # Check if there's a winner

    if b == 9 and c == 0:  # Check for a draw
        tkinter.messagebox.showinfo("Tic Tac Toe", "Match is a Draw!")
        disable_buttons()

# Check for Winner
def check_winner():
    global c
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    for combo in winning_combinations:
        if (buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"]) and buttons[combo[0]]["text"] != " ":
            c = 1
            winner = "Player 1" if buttons[combo[0]]["text"] == "X" else "Player 2"
            tkinter.messagebox.showinfo("Tic Tac Toe", f"Winner is {winner}!")
            disable_buttons()
            break

# Create Buttons
buttons = []
for i in range(9):
    button = Button(root, text=" ", font=("Helvetica", 20), width=5, height=2)
    button.grid(row=i // 3, column=i % 3, sticky="nsew", ipadx=40, ipady=40)
    button.config(command=lambda id=i + 1: buttonclick(id))
    buttons.append(button)

# Labels and Restart Button
playerturn = ttk.Label(root, text="Player 1 Turn!", font=("Helvetica", 12))
playerturn.grid(row=3, column=0, sticky="nsew", ipadx=40, ipady=20)

playerdetails = ttk.Label(root, text="Player 1 is X\nPlayer 2 is O", font=("Helvetica", 12))
playerdetails.grid(row=3, column=2, sticky="nsew", ipadx=40, ipady=20)

res = ttk.Button(root, text="Restart", command=restartbutton)
res.grid(row=3, column=1, sticky="nsew", ipadx=40, ipady=20)

# Run the Game
root.mainloop()