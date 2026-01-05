'''
Rock, Paper, Scissors
Given two strings, the first representing Player 1 and the second representing Player 2, determine the winner of a match of Rock, Paper, Scissors.

The input strings will always be "Rock", "Paper", or "Scissors".
"Rock" beats "Scissors".
"Paper" beats "Rock".
"Scissors" beats "Paper".
Return:

"Player 1 wins" if Player 1 wins.
"Player 2 wins" if Player 2 wins.
"Tie" if both players choose the same option.
'''


def rock_paper_scissors(player1, player2):
    rules = {
        "Rock": "Scissors",
        "Paper": "Rock",
        "Scissors": "Paper"
    }
    result = None
    if player1 == player2:
        result = "Tie"
        # return result
    elif rules[player1] == player2:
        result = "Player 1 wins"
    else:
        result = "Player 2 wins"
    print(result)
    player1 = result
    return player1

t = rock_paper_scissors("Rock", "Paper")
print(t)

t1 = rock_paper_scissors("Rock", "Rock")
print(t1)