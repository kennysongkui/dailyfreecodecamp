'''
Tic-Tac-Toe
Given a 3×3 matrix (an array of arrays) representing a completed Tic-Tac-Toe game, determine the winner.

Each element in the given matrix is either an "X" or "O".
A player wins if they have three of their characters in a row - horizontally, vertically, or diagonally.

Return:

"X wins" if player X has three in a row.
"O wins" if player O has three in a row.
"Draw" if no player has three in a row.
'''


def tic_tac_toe(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "":
            return f"{row[0]} wins"

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '':
            return f"{board[0][col]} wins"

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return f"{board[0][0]} wins"

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return f"{board[0][2]} wins"

    result = "Draw"
    board = result

    return board


t = tic_tac_toe([["X", "X", "X"], ["O", "O", "X"], ["O", "X", "O"]])
print(t)
