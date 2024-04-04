#!/user/zhao/miniconda3/envs/torch-0
# -*- coding: utf_8 -*-
# @Time : 2024/4/3 16:22
# @Author: ZhaoKe
# @File : CommonAncestors.py
# @Software: PyCharm
from collections import deque
from typing import List

from datasets.generate_graph import get_graph_1, get_graph_2
from datastructures.graph_entities import Vertex, Edge
from datastructures.AdjListGraph import AdjListGraph


# from datastructures.Ad


def find_all_post(graph: AdjListGraph, v: Vertex) -> List[tuple]:
    marked = [False] * len(graph)
    que = deque()
    Li = [(v, 0)]
    marked[v.index] = True
    que.append((v, 0))
    while len(que) > 0:
        t, depth = que.popleft()
        for child in graph.children[t.index]:
            if not marked[child.index]:
                Li.append((child, depth + 1))
                marked[child.index] = True
                que.append((child, depth + 1))
    return Li


def find(graph: AdjListGraph, v: Vertex) -> List[tuple]:
    marked = [False] * len(graph)
    que = deque()
    Li = [(v, 0)]
    marked[v.index] = True
    # 直接后继直接添加
    for child in graph.children[v.index]:
        marked[child.index] = True
        que.append((child, 1))
        # if len(graph.children[])
        Li.append((child, 1))

    # 后续的后继就要判断是不是被当前点隔绝的了，是的话不能加，那称不上是共同祖先，
    while len(que) > 0:
        t, depth = que.popleft()
        for child in graph.children[t.index]:
            if not marked[child.index]:
                marked[child.index] = True
                que.append((child, depth + 1))

                # 入度是1的节点不能算共同祖先，它只是流经的一条边
                # 不行，即使跳过了该点，该点的后继也不好判断，还是得分层，割点后面的都得抛去
                if graph.indegree[child.index] == 1:  # and graph.outdegree[child.index] == 1:
                    pass
                else:
                    Li.append((child, depth + 1))
    return Li


def find_all_ca(graph: AdjListGraph, v: Vertex, w: Vertex) -> List[Vertex]:
    print("----find nearest common ancestor----")
    # 图的边全部逆转，得到新的图
    inv_graph = graph.reverse_graph()
    # 找到两个节点的所有前驱节点及对应的节点跳数
    Lv = find(inv_graph, v)
    Lw = find(inv_graph, w)
    # print(v.name, w.name)
    # print([(item.name, depth) for (item, depth) in Lv])
    # print([(item.name, depth) for (item, depth) in Lw])

    # 求交集（可以优化的点，并查集，我现在是O(n2)）
    # 创建字典：节点1的节点与条数
    cnt = dict()
    for item, depth in Lv:
        cnt[item.name] = (item, depth)
    # print("init:", cnt)
    # 留下节点2也有的
    uni = [True] * len(cnt.keys())
    for j, (item, depth) in enumerate(Lw):
        if item.name in cnt.keys():
            cnt[item.name] = (item, cnt[item.name][1]+depth)
            for k, it in enumerate(Lv):
                # print(it[0].name, item.name)
                if it[0].name == item.name:
                    uni[k] = False
                    break
            # uni[j] = False
    # print("after intersection:", uni)

    # 删去节点2没有的，得到交集
    for j in range(len(uni)):
        if uni[j] is True:
            del cnt[Lv[j][0].name]
    # 根据跳数排序，
    cnt = sorted(cnt.items(), key=lambda s: s[1][1])
    for j, item in cnt:
        print(j, item[0])

    # # find nearest common ancestors:
    # for j, (item, depth) in enumerate(Lw):
    #     if item.name in cnt.keys():
    #         return Lv[j]

    # find all common ancestors:
    res = []
    for _, item in cnt:
        if item[1] > 0:
            print(item[0])
            res.append(item)
    return res


if __name__ == '__main__':
    G = get_graph_1()
    # G.print_edges()
    res = find_all_ca(graph=G, v=Vertex(6, "K"), w=Vertex(7, "L"))
    for item in res:
        print(item)

    G = get_graph_2()
    # G.print_edges()
    res = find_all_ca(graph=G, v=Vertex(5, "S"), w=Vertex(6, "D"))
    for item in res:
        print(item)
    # inv_g = G.reverse_graph()
    # inv_g.print_edges()
