'''
Domino Chain Validator
Given a 2D array representing a sequence of dominoes, determine whether it forms a valid chain.

Each element in the array represents a domino and will be an array of two numbers from 1 to 6, (inclusive).
For the chain to be valid, the second number of each domino must match the first number of the next domino.
The first number of the first domino and the last number of the last domino don't need to match anything.

'''


def is_valid_domino_chain(dominoes):
    arr_len = len(dominoes)
    for i in range(arr_len - 1):
        print(i)
        # x, y = dominoes[i]

        print(dominoes[i][1])

        if dominoes[i][1] != dominoes[i + 1][0]:
            return False

        # print(x, y)

    result = True
    dominoes = result

    return dominoes


t = is_valid_domino_chain([[1, 3], [3, 6], [6, 5]])
print(t)
