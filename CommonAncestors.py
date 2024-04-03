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


def find(graph: AdjListGraph, v: Vertex) -> List[tuple]:
    marked = [False] * len(graph)
    que = deque()
    Li = [(v, 0)]
    marked[v.index] = True
    que.append((v, 0))
    while len(que) > 0:
        t, depth = que.popleft()
        for child in graph.children[t.index]:
            if not marked[child.index]:
                Li.append((child, depth+1))
                marked[child.index] = True
                que.append((child, depth+1))
    return Li


def find_all_ca(graph: AdjListGraph, v: Vertex, w: Vertex) -> List[Vertex]:
    print("----find nearest common ancestor----")
    inv_graph = graph.reverse_graph()
    Lv = find(inv_graph, v)
    Lw = find(inv_graph, w)
    # print(v.name, w.name)
    # print([(item.name, depth) for (item, depth) in Lv])
    # print([(item.name, depth) for (item, depth) in Lw])

    cnt = dict()
    for item, depth in Lv:
        cnt[item.name] = depth

    # # find nearest common ancestors:
    # for j, (item, depth) in enumerate(Lw):
    #     if item.name in cnt.keys():
    #         return Lv[j]

    # find all common ancestors:
    for item, depth in Lw:
        if item.name in cnt.keys():
            cnt[item.name] += depth
    cnt = sorted(cnt.items(), key=lambda s:s[1])
    res = []
    for j, item in enumerate(cnt):
        if item[1] > 0:
            # print(item)
            res.append(Lv[j][0])
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
