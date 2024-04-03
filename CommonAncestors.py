#!/user/zhao/miniconda3/envs/torch-0
# -*- coding: utf_8 -*-
# @Time : 2024/4/3 16:22
# @Author: ZhaoKe
# @File : CommonAncestors.py
# @Software: PyCharm
from collections import deque
from typing import List

from datastructures.graph_entities import Vertex, Edge
from datastructures.AdjListGraph import AdjListGraph
# from datastructures.Ad


def find(graph: AdjListGraph, v: Vertex) -> List[Vertex]:
    marked = [False] * len(graph)
    que = deque()
    Li = []
    marked[v.index] = True
    que.append(v)
    while len(que) > 0:
        t = que.popleft()
        for child in graph.children[t.index]:
            if not marked[child.index]:
                Li.append(child)
                marked[child.index] = True
                que.append(child)
    return Li


def find_nestest_ca(graph: AdjListGraph, v: Vertex, w: Vertex) -> Vertex:
    print("----find nearest common ancestor----")
    inv_graph = graph.reverse_graph()
    Lv = find(inv_graph, v)
    Lw = find(inv_graph, w)
    if len(Lv) > len(Lw):
        for t in Lw:
            if t in Lv:
                return t
    else:
        for t in Lv:
            if t in Lw:
                return t
    return None


if __name__ == '__main__':
    G = AdjListGraph(num_ver=6)
    # print_matrix(G.adj_matrix)
    G.add_edge(Edge(0, 2, 3, 2))
    G.add_edge(Edge(1, 0, 1, 1))
    G.add_edge(Edge(2, 0, 2, 1))
    G.add_edge(Edge(3, 1, 4, 1))
    G.add_edge(Edge(4, 1, 3, 1))
    G.add_edge(Edge(5, 3, 5, 1))
    G.print_edges()

    res = find_nestest_ca(graph=G, v=Vertex(5), w=Vertex(4))
    print(res)

    # inv_g = G.reverse_graph()
    # inv_g.print_edges()
