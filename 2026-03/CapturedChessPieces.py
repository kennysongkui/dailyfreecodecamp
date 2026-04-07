'''
Captured Chess Pieces
Given an array of strings representing chess pieces you still have on the board, calculate the value of the pieces your opponent has captured.

In chess, you start with 16 pieces:

Piece	Abbreviation	Quantity	Value
Pawn	"P"	8	1
Rook	"R"	2	5
Knight	"N"	2	3
Bishop	"B"	2	3
Queen	"Q"	1	9
King	"K"	1	0
The given array will only contain the abbreviations above.
Any of the 16 pieces not included in the given array have been captured.
Return the total value of all captured pieces, unless...
If the King has been captured, return "Checkmate".
'''

def get_captured_value(pieces):

    start_counts = {'P':8, "R":2, "N":2, "B":2, "Q":1,"K":1}
    values = {"P":1, "R":5, "N":3, "B":3, "Q":9, "K":0}

    remaining_counts = {}
    for i in pieces:
        remaining_counts[i] = remaining_counts.get(i, 0) + 1

    if remaining_counts.get('K',0) == 0:
        return "Checkmate"

    remaining_value = 0
    for piece, count in remaining_counts.items():
        remaining_value += values[piece] * count

    start_value = 39
    result = start_value - remaining_value
    print(result)

    pieces = result

    return pieces

t = get_captured_value(["P", "P", "P", "P", "P", "P", "R", "R", "N", "B", "Q", "K"])
print(t)