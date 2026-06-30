'''
FizzBuzz Explosion
Given an integer, return the number of steps it takes to turn the word "fizzbuzz" into a string with at least the given number of "z"'s using the following rules:

Start with the string "fizzbuzz".
Each step, apply the standard FizzBuzz rules using the letter position in the string (the first "f" is position 1).
If the letter position is divisible by 3, replace the letter with "fizz"
If it's divisible by 5, replace the letter with "buzz"
If it's divisible by 3 and 5, replace the letter with "fizzbuzz"
So after 1 step, "fizzbuzz" turns into "fifizzzbuzzfizzzz", which has 9 "z"'s.
'''


def explode_fizzbuzz(target_z_count):
    s = "fizzbuzz"
    steps = 0

    while s.count('z') < target_z_count:
        parts = []
        for i, ch in enumerate(s, start=1):
            if i % 15 == 0:
                parts.append("fizzbuzz")
            elif i % 3 == 0:
                parts.append("fizz")
            elif i % 5 == 0:
                parts.append("buzz")
            else:
                parts.append(ch)
        s = ''.join(parts)
        steps += 1

    print(steps)
    target_z_count = steps
    return target_z_count


# t = explode_fizzbuzz(9)
# print(t)

t1 = explode_fizzbuzz(15)
print(t1)