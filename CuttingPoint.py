# -*- coding: utf-8 -*-
# @Author : ZhaoKe
# @Time : 2024-04-05 12:46
from collections import deque
from math import log2
from typing import List


def print_matrix(matrix: List[List]):
    print("---" * len(matrix))
    for row in matrix:
        print(row)
    print("---" * len(matrix))


def log2_int(n: int) -> int:
    res = 0
    while n > 0:
        n >>= 1
        res += 1
    return res


def matrix_add(matrix: List[List], num: int):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] += num


def lowbit(n: int) -> int:
    # n&(n-1)： 最右边的1改为0
    # 保留n最右边的1
    # print(lowbit(15))  # 0001
    return n & (-n)


def highbit(n: int) -> int:
    # print(highbit(15))  # 1000
    p = lowbit(n)
    while p != n:
        n -= p
        p = lowbit(n)
    return p


def lca(x: int, y: int, d: List[int], f: List[List]) -> int:
    if d[x] < d[y]:
        return lca(y, x, d, f)
    delta = d[x] - d[y]
    while delta > 0:
        x = f[x][log2_int(highbit(delta))]
        delta -= highbit(delta)
    if x == y:
        return x
    n = len(d)
    m = log2_int(n)
    while True:
        if [x][0] == f[y][0]:
            break
        k = 1
        while k <= m:
            if f[x][k] == -1 or f[y][k] == -1:
                break
            if f[x][k] == f[y][k]:
                break
            k += 1
        x = f[x][k - 1]
        y = f[y][k - 1]
    return f[x][0]


def dfs(DT: List[List], u: int, result: List) -> int:
    size = 1
    for v in DT[u]:
        size += dfs(DT, v, result)
    result[u] = size - 1
    return size


def dg_main():
    """
    reference: https://blog.csdn.net/u011472272/article/details/109038476
    :return:
    """
    edges = [
        [0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [3, 5], [4, 6], [4, 7], [5, 6], [5, 7]
    ]
    n = 8
    D = [[] for _ in range(8)]
    for i, edge in enumerate(edges):
        D[edge[0]].append(edge[1])
    for ver in D:
        print(ver)
    RD = [[] for _ in range(n)]
    for i, children in enumerate(D):
        for item in children:
            RD[item].append(i)
    # 超级源
    matrix_add(D, 1)
    matrix_add(RD, 1)
    D.insert(0, [])
    RD.insert(0, [])
    # RD.append([])
    print(D)
    print(RD)
    # n -= 1
    indegree = [0] * (n + 1)
    for i in range(1, n + 1):
        if len(RD[i]) == 0:
            RD[i].append(0)
            D[0].append(i)
        indegree[i] = len(RD[i])
    print_matrix(D)
    print_matrix(RD)
    # 寻找原图拓扑序
    topo_order = []
    q = deque()
    q.append(0)
    while len(q) > 0:
        u = q.popleft()
        topo_order.append(u)
        for v in D[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    print("topo order:")
    print(topo_order)

    DT = [[] for _ in range(n + 1)]
    # 2^m <= n
    # log2(2^m) <= log2(n)
    # m <= log2(n)
    m = int(log2(n))
    f = [[-1] * (m + 1) for _ in range(n + 1)]
    d = [-1] * (n + 1)
    d[0] = 0
    for u in topo_order:
        if len(RD[u]) == 0:
            continue
        k = len(RD[u])
        idom = RD[u][0]
        for j in range(1, k):
            fa = RD[u][j]
            idom = lca(idom, fa, d, f)
        DT[idom].append(u)
        f[u][0] = idom
        d[u] = d[idom] + 1
        p = 1
        while (p <= m and f[f[u][p - 1]][p - 1] != -1):
            f[u][p] = f[f[u][p - 1]][p - 1]
            p += 1
    result = [0] * (n + 1)
    print("=====DT======")
    print_matrix(DT)

    print("---->f")
    print(f)
    print("---->d")
    print(d)
    dfs(DT, 0, result)
    print(result)
    # for u in range(1, n + 1):
    #     print(result)


if __name__ == '__main__':
    dg_main()
    # print(log2_int(7))
    # print(log2_int(14))
    # print(log2_int(19))
    # edges = [[0, 1], [0,2],[0,3],
    #                                  [1, 4],
    #                                  [2, 1], [2, 4], [2,5],
    #                                  [3, 6], [3,7],
    #                                  [4, 12],
    #                                  [5, 8],
    #                                  [6, 9],
    #                                  [7, 9],[7, 10],
    #                                  [8, 5], [8,11],[9,11], [10, 9], [11, 0],[11,9], [12, 8]]
    # n = 13
    # D = [[] for _ in range(13)]
    # for i, edge in enumerate(edges):
    #     D[edge[0]].append(edge[1])
    # for ver in D:
    #     print(ver)

    # G = get_graph_1()
    # G = G.reverse_graph()
    # G.print_edges()
    # print(G.deep)
    # G.topoSort()

    # res = find_all_ca(graph=G, v=Vertex(6, "K"), w=Vertex(7, "L"))
    # for item in res:
    #     print(item)

    # udg = UnDirectedGraph(num_ver=7, adj_matrix=[
    #     [1, 2],
    #     [0, 3],
    #     [0, 3],
    #     [1, 2, 4, 5],
    #     [3, 6],
    #     [3, 6],
    #     [4, 5]])
    # cs = udg.find_AP()
    # print(cs)

    # dg = AdjListGraph(vertices=[Vertex], num_ver=8)
    # dg.children = [
    #     [1, 2],
    #     [3],
    #     [3],
    #     [4, 5],
    #     [6, 7],
    #     [6, 7],
    #     [],
    #     []]
    # cs = dg.topoSort()
    # print(cs)
