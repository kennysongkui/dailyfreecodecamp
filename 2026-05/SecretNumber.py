'''
Secret Number
Given a secret number and a guess, determine if the guess is correct.

Return:

"higher" if the secret number is higher than the guess.
"lower" if the secret number is lower than the guess.
"you got it!" if the guess is correct.
'''

def guess_number(secret, guess):

    if secret > guess:
        return 'higher'
    elif secret < guess:
        return 'lower'
    elif secret == guess:
        return 'you got it!'

    return secret

t = guess_number(50, 30)
print(t)