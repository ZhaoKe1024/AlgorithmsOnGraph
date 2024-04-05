# -*- coding: utf-8 -*-
# @Author : ZhaoKe
# @Time : 2024-04-05 23:32
# reference: https://oi-wiki.org/graph/dominator-tree/
# https://www.cnblogs.com/downrainsun/p/11221684.html
from typing import List

edge = [
    [1],
    [2, 4, 5],
    [3],
    [4],
    [],
    [6, 8],
    [7],
    [],
    [7]
]

pre = [
    [],
    [0],
    [1],
    [2],
    [1, 3],
    [1],
    [5],
    [6, 8],
    [5]
]
ord_list = [7, 8, 6, 5, 4, 3, 2, 1, 0]


def _dfs(u: int, del_v: int, vis: List[bool]):
    vis[u] = True
    for v in edge[u]:
        if v == del_v or vis[v]:
            continue
        _dfs(v, del_v, vis)


def getdom():
    N = 9
    dom = [[] for _ in range(N)]
    for i in range(1, N):
        # global vis  # 不加这句真不行
        vis = [False] * N
        _dfs(0, i, vis)
        for j in range(0, N):
            if not vis[j]:
                dom[j].append(i)
    for item in dom:
        print(item)


def bool_array_intersect(array1, array2):
    res = [False] * len(array2)
    for i in range(len(array1)):
        res[i] = array1[i] and array2[i]
    return res


def bool_array_eq(array1, array2) -> bool:
    res = True
    for i in range(len(array1)):
        res &= (array1[i] and array2[i])
    return res


def get_dom_1():
    N = 9
    dom = [[False] * N for _ in range(N)]
    Dom = [[] for _ in range(N)]
    dom[0][0] = True
    flag = True
    while flag:
        flag = False
        for u in ord_list:
            tmp = [False] * N
            tmp[u] = True
            for v in pre[u]:
                tmp = bool_array_intersect(tmp, dom[v])
            if not bool_array_eq(tmp, dom[u]):
                dom[u] = tmp
                flag = True
    for i in range(1, N):
        for j in range(0, N):
            if dom[i][j]:
                Dom[i].append(j)
    for item in Dom:
        print(item)


if __name__ == '__main__':
    getdom()
    # get_dom_1()
    # print(vis)
