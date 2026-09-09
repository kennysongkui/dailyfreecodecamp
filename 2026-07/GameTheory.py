'''
Game Theory
Given two equal length strings representing two players' strategies for a game, return the scores as an array [player1, player2].

The given strings will only contain one of two letters: "C" (cooperate) or "D" (defect).
Each character represents one round, scored as follows:
If both players cooperate, each scores 3.
If both players defect, each scores 1.
If one player defects and the other cooperates, the defector scores 5 and the cooperator scores 0.
'''

def play_game(p1, p2):
    p_len = len(p1)
    total_p1, total_p2 = 0,0
    for i in range(p_len):
        if p1[i] == p2[i]:
            if p1[i] == 'C':
                total_p1 += 3
                total_p2 += 3
            else:
                total_p1 += 1
                total_p2 += 1
        else:
            if p1[i] == 'C':
                total_p2 += 5
            else:
                total_p1 += 5
    print(total_p1, total_p2)
    result = [total_p1, total_p2]
    p1 = result
    return p1

t = play_game("CCCC", "CCCC")
print(t)