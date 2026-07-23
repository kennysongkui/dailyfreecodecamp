'''
Longest Common Substring
Given a string, return the longest substring that appears more than once.

The substrings can overlap.
'''


def get_longest_substring(s):

    n = len(s)
    if n < 2:
        return ""

    sa = build_sa(s)
    lcp = kasai(s, sa)

    if not lcp:
        return ""

    max_len = max(lcp)
    if max_len == 0:
        return ""

    idx= lcp.index(max_len)
    start = sa[idx]
    result = s[start:start + max_len]
    print(result)
    s = result
    return s


def build_sa(s):
    n = len(s)
    k = 1
    sa = list(range(n))
    rank = list(map(ord, s))
    tmp = [0] * n

    while True:
        sa.sort(key=lambda x: (rank[x], rank[x + k] if x + k < n else -1))
        tmp[sa[0]] = 0
        for j in range(1, n):
            prev, cur = sa[j - 1], sa[j]
            prev_second = rank[prev + k] if prev + k < n else -1
            cur_second = rank[cur + k] if cur + k < n else -1
            tmp[cur] = tmp[prev] + (rank[cur] != rank[prev] or cur_second != prev_second)
        rank, tmp = tmp, rank
        if rank[sa[-1]] == n - 1:
            break
        k <<= 1
    return sa


def kasai(s, sa):
    n = len(s)
    rank = [0] * n
    for i in range(n):
        rank[sa[i]] = i

    lcp = [0] * (n - 1)
    h = 0
    for i in range(n):
        if rank[i] == 0:
            continue
        j = sa[rank[i] - 1]
        while i + h < n and j + h < n and s[i + h] == s[j + h]:
            h += 1
        lcp[rank[i] - 1] = h
        if h:
            h -= 1
    return lcp


t = get_longest_substring("abracadabra")
print(t)
