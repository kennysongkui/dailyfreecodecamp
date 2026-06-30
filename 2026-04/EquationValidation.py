'''
Equation Validation
Given a string representing a math equation, determine whether it is correct.

The left side may contain up to three positive integers and the operators +, -, *, and /.
The equation will be given in the format: "number operator number = number" (with two or three numbers on the left). For example: "2 + 2 = 4" or "2 + 3 - 1 = 4".
The right side will always be a single integer.
Follow standard order of operations: multiplication and division are evaluated before addition and subtraction, from left-to-right.
'''

from fractions import Fraction
def is_valid_equation(equation):
    parts = equation.split()

    eq_index = parts.index("=")
    left_tokens = parts[:eq_index]
    right_value = int(parts[eq_index + 1])

    print(eq_index,left_tokens, right_value )

    nums = []
    ops = []
    for i, token in enumerate(left_tokens):
        if i % 2 == 0:
            nums.append(int(token))
        else:
            ops.append(token)

    print(nums, ops)
    new_nums = [Fraction(nums[0])]
    new_ops = []

    for i , op in enumerate(ops):
        if op == "*" or op == "/":
            if op == "*":
                new_nums[-1] *= nums[i+1]
            else:
                new_nums[-1] /= nums[i+1]
        else:
            new_ops.append(op)
            new_nums.append(Fraction(nums[i+1]))

    print(new_nums, new_ops)
    result = new_nums[0]

    for i, op in enumerate(new_ops):
        if op == '+':
            result += new_nums[i+1]
        else:
            result -= new_nums[i+1]

    print(result, right_value)


    if result == right_value:
        flag = True
    else:
        flag = False

    print(flag)
    equation = flag

    return equation

# t = is_valid_equation("2 + 2 = 4")
# print(t)

t1 = is_valid_equation("2 + 3 - 1 = 4")
print(t1)