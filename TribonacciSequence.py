'''
Tribonacci Sequence
The Tribonacci sequence is a series of numbers where each number is the sum of the three preceding ones. When starting with 0, 0 and 1, the first 10 numbers in the sequence are 0, 0, 1, 1, 2, 4, 7, 13, 24, 44.

Given an array containing the first three numbers of a Tribonacci sequence, and an integer representing the length of the sequence, return an array containing the sequence of the given length.

Your function should handle sequences of any length greater than or equal to zero.
If the length is zero, return an empty array.
Note that the starting numbers are part of the sequence.
'''


def tribonacci_sequence(start_sequence, length):
    if length == 0:
        length = []
    elif length == 1:
        length = [start_sequence[0]]
    elif length == 2:
        length = [start_sequence[0], start_sequence[1]]
    elif length == 3:
        length = start_sequence[:]
    else:
        i = 3

        while i < length:
            e = start_sequence[i - 3] + start_sequence[i - 2] + start_sequence[i - 1]
            start_sequence.append(e)
            # print(e)
            i = i + 1
            # print(i)
        length = start_sequence[:]

    return length


# t = tribonacci_sequence([21, 32, 43], 1)
# print(t)
#
# t1 = tribonacci_sequence([0, 0, 1], 20)
# print(t1)
t2 = tribonacci_sequence([123, 456, 789], 8)
print(t2)
