'''
Missing Socks
Given an integer representing the number of pairs of socks you started with, and another integer representing how many wash cycles you have gone through, return the number of complete pairs of socks you currently have using the following constraints:

Every 2 wash cycles, you lose a single sock.
Every 3 wash cycles, you find a single missing sock.
Every 5 wash cycles, a single sock is worn out and must be thrown away.
Every 10 wash cycles, you buy a pair of socks.
You can never have less than zero total socks.
Rules can overlap. For example, on wash cycle 10, you will lose a single sock, throw away a single sock, and buy a new pair of socks.
Return the number of complete pairs of socks.
'''

def sock_pairs(pairs, cycles):
    total_socks = pairs * 2

    for i in range(1, cycles+ 1):
        if i % 2 == 0:
            total_socks = max(0, total_socks -1)

        if i % 3 == 0:
            total_socks += 1

        if i % 5 == 0:
            total_socks = max(0, total_socks -1)
        if i % 10 == 0:
            total_socks += 2

    pairs = total_socks // 2
    return pairs

t = sock_pairs(2, 5)
print(t)

t1 = sock_pairs(6, 25)
print(t1)