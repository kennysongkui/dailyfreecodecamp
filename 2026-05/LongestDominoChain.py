'''
Longest Domino Chain
Given a 2D array representing a set of dominoes, return the longest valid chain.

Each domino is a pair of numbers from 0–6, e.g. [3, 2].
A chain is valid when the second number of each domino matches the first number of the next.
The first number of the first domino and the second number of the last one don't need to match anything.
Any domino can be flipped, so [3, 2] can be played as [2, 3].
There is always exactly one longest valid chain.
For example, given [[1, 2], [4, 5], [2, 3]], return [[1, 2], [2, 3]].
'''


def get_longest_chain(dominoes):
    # 统计非自环和多米诺骨牌的数量
    # c[u][v] 表示无序对 (u, v) 的个数 (u < v)
    c = [[0] * 7 for _ in range(7)]
    self_count = [0] * 7

    for a, b in dominoes:
        if a == b:
            self_count[a] += 1
        else:
            u, v = sorted((a, b))
            c[u][v] += 1

    # 所有可能的无序对（非自环，且数量 > 0）
    all_pairs = [(u, v) for u in range(7) for v in range(u + 1, 7) if c[u][v] > 0]

    best_len = 0
    best_T = 0  # 顶点子集（位掩码）
    best_mask = 0  # 对应 best_T 中每个无序对是否删除一条边
    best_P = []  # best_T 中涉及的无序对列表

    # 枚举所有非空顶点子集 T（位掩码）
    for T in range(1, 1 << 7):
        vertices = [v for v in range(7) if (T >> v) & 1]
        # 只保留两端都在 T 中的无序对
        P = [(u, v) for (u, v) in all_pairs if ((T >> u) & 1) and ((T >> v) & 1)]
        m = len(P)

        # 若 T 中没有非自环边，则只有可能由自环组成链
        if m == 0:
            total = sum(self_count[v] for v in vertices)
            if total > best_len:
                best_len = total
                best_T = T
                best_mask = 0
                best_P = []
            continue

        # 对每个无序对，选择是否删除一条边（0 或 1 条）
        for mask in range(1 << m):
            deg = [0] * 7
            kept_pairs = []  # 保留的非自环边（用于连通性检查）
            # 计算保留的边数和度数
            for i, (u, v) in enumerate(P):
                drop = (mask >> i) & 1
                k = c[u][v] - drop
                if k > 0:
                    deg[u] += k
                    deg[v] += k
                    kept_pairs.append((u, v))

            # 如果没有保留任何非自环边，则只能 T 中只有一个顶点才可能连通
            if not kept_pairs:
                if len(vertices) == 1:
                    total = sum(self_count[v] for v in vertices)
                    if total > best_len:
                        best_len = total
                        best_T = T
                        best_mask = mask
                        best_P = P
                continue

            # 检查保留的图在 T 上是否连通（BFS）
            start = vertices[0]
            visited = 0
            stack = [start]
            visited |= (1 << start)
            while stack:
                v = stack.pop()
                for u, w in kept_pairs:
                    if u == v and not ((visited >> w) & 1):
                        visited |= (1 << w)
                        stack.append(w)
                    elif w == v and not ((visited >> u) & 1):
                        visited |= (1 << u)
                        stack.append(u)
            if visited != T:
                continue

            # 检查奇度顶点个数是否为 0 或 2
            odd_count = 0
            for v in vertices:
                if deg[v] % 2 == 1:
                    odd_count += 1
            if odd_count == 0 or odd_count == 2:
                total_non_self = sum(deg[v] for v in vertices) // 2
                total = total_non_self + sum(self_count[v] for v in vertices)
                if total > best_len:
                    best_len = total
                    best_T = T
                    best_mask = mask
                    best_P = P

    # 如果没有任何多米诺骨牌，返回空列表
    if best_len == 0:
        return []

    # 根据最优参数重建链
    vertices = [v for v in range(7) if (best_T >> v) & 1]
    edges = []  # 存储所有要使用的边（含自环），每条边作为一个元组 (u, v)

    # 添加非自环边
    for i, (u, v) in enumerate(best_P):
        drop = (best_mask >> i) & 1
        k = c[u][v] - drop
        if k > 0:
            edges.extend([(u, v)] * k)

    # 添加自环
    for v in vertices:
        edges.extend([(v, v)] * self_count[v])

    if not edges:
        return []

    # 构建边的计数（用于 Hierholzer 算法）
    edge_count = {}
    for u, v in edges:
        key = (min(u, v), max(u, v))
        edge_count[key] = edge_count.get(key, 0) + 1

    # 计算度数以确定起点
    deg = [0] * 7
    for u, v in edges:
        deg[u] += 1
        deg[v] += 1

    odd_vertices = [v for v in range(7) if deg[v] % 2 == 1]
    if odd_vertices:
        start = odd_vertices[0]
    else:
        start = next((v for v in range(7) if deg[v] > 0), None)
        if start is None:
            return []

    # Hierholzer 算法求欧拉路径
    stack = [start]
    path = []
    while stack:
        v = stack[-1]
        found = False
        for u in range(7):
            key = (min(v, u), max(v, u))
            if edge_count.get(key, 0) > 0:
                edge_count[key] -= 1
                stack.append(u)
                found = True
                break
        if not found:
            path.append(stack.pop())

    trail = path[::-1]  # 倒序得到顶点顺序

    # 生成多米诺骨牌链
    result = []
    for i in range(len(trail) - 1):
        result.append([trail[i], trail[i + 1]])

    print(result)

    dominoes = result

    return dominoes


t = get_longest_chain([[1, 2], [4, 5], [2, 3]])
print(t)
