'''
Perfect Cube Count
Given two integers, determine how many perfect cubes exist in the range between and including the two numbers.

The lower number is not garanteed to be the first argument.
A number is a perfect cube if there exists an integer (n) where n * n * n = number. For example, 27 is a perfect cube because 3 * 3 * 3 = 27.
'''


def count_perfect_cubes(a, b):
    low = min(a, b)
    high = max(a, b)

    k_end = floor_cbrt(high)

    fc_low = floor_cbrt(low)

    if fc_low * fc_low * fc_low >= low:
        k_start = fc_low
    else:
        k_start = fc_low + 1
    if k_start > k_end:
        return 0
    result = k_end - k_start + 1

    a = result
    return a


def floor_cbrt(x):
    if x == 0:
        return 0
    sign = 1 if x > 0 else -1
    a = abs(x)
    lo, hi = 0, a
    while lo  <= hi:
        mid = (lo + hi) //2
        cube = mid * mid * mid
        if cube == a:
            lo = mid
            break
        elif cube < a:
            lo = mid +1
        else:
            hi = mid -1

    n_pos = hi
    if sign == 1:
        return n_pos
    else:
        if n_pos * n_pos * n_pos == a:
            return -n_pos
        else:
            return -(n_pos + 1)

t = count_perfect_cubes(3, 30)
print(t)
