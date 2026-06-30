'''
Prank Number
Given an array of numbers where all but one number follow a pattern, return a new array with the one number that doesn't follow the pattern fixed.

The pattern will be one of:

The numbers increase from one to the next by a fixed amount (addition).
The numbers decrease from one to the next by a fixed amount (subtraction).
For example, given [2, 4, 7, 8, 10] return [2, 4, 6, 8, 10].
'''

from collections import Counter
def fix_prank_number(arr):

    n = len(arr)
    if n <= 2:
        # 长度不足时无法判断，直接返回原数组（题目保证至少3个元素）
        return arr[:]

    # 1. 计算所有相邻差值，找出出现频率最高的差值作为正确的公差 d
    diffs = [arr[i+1] - arr[i] for i in range(n-1)]
    d = Counter(diffs).most_common(1)[0][0]
    print(d)

    # 2. 尝试以第一个元素为起点构建等差数列
    expected = [arr[0] + i * d for i in range(n)]
    # 找出原数组与预期数组不同的位置
    error_indices = [i for i in range(n) if arr[i] != expected[i]]

    if len(error_indices) == 1:
        # 只有一个位置不同，说明第一个元素是正确的，直接修正那个错误元素
        return expected
    else:
        # 第一个元素本身错误，改用第二个元素反推正确的起点
        correct_start = arr[1] - d
        corrected = [correct_start + i * d for i in range(n)]
        return corrected



    return arr


# t = fix_prank_number([2, 4, 7, 8, 10])
# print(t)
#
# t1 = fix_prank_number([10, 10, 8, 7, 6])
# print(t1)
#
# t2 = fix_prank_number([12, 24, 36, 48, 61, 72, 84, 96])
# print(t2)

t3 = fix_prank_number([4, 1, -2, -5, -8, -5])
print(t3)
