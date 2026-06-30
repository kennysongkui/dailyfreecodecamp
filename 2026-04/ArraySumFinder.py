'''
Array Sum Finder
Given an array of numbers and a target number, return the first subset of two or more numbers that adds up to the target.

The "first" subset is the one whose elements have the lowest possible indices, prioritizing the earliest index first.
Each number in the array may only be used once.
If no valid subset exists, return "Sum not found".
Return the matching numbers as an array in the order they appear in the original array.
'''


def find_sum(arr, target):
    n = len(arr)
    selected = []  # 记录选中元素的索引
    result = None

    def dfs(start, cur_sum):
        nonlocal result
        # 如果已经找到结果，提前终止
        if result is not None:
            return True
        # 检查当前是否满足条件（大小≥2且和等于目标）
        if cur_sum == target and len(selected) >= 2:
            result = selected[:]  # 保存索引的副本
            return True
        # 如果已经处理完所有元素
        if start == n:
            return False

        # 先尝试选择当前元素
        selected.append(start)
        if dfs(start + 1, cur_sum + arr[start]):
            return True
        selected.pop()

        # 再尝试不选当前元素
        if dfs(start + 1, cur_sum):
            return True

        return False

    dfs(0, 0)

    if result is None:
        return "Sum not found"
    # 按索引顺序返回对应的数值
    return [arr[i] for i in result]

    return arr

# t = find_sum([1, 3, 5, 7], 6)
# print(t)

t1 = find_sum([1, 2, 3, 4, 5], 6)
print(t1)