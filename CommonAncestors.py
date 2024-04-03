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
                Li.append((child, depth+1))
                marked[child.index] = True
                que.append((child, depth+1))
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

                que.append((child, depth+1))
                # 判断当前节点是不是瓶颈点，也就是后面所有节点都要流经该点
                # 方法很简单: 所有孩子节点的入度都是1
                # if len(graph.children[])
                Li.append((child, depth+1))
    return Li


def find_all_ca(graph: AdjListGraph, v: Vertex, w: Vertex) -> List[Vertex]:
    print("----find nearest common ancestor----")
    # 图的边全部逆转，得到新的图
    inv_graph = graph.reverse_graph()
    # 找到两个节点的所有前驱节点及对应的节点跳数
    Lv = find(inv_graph, v)
    Lw = find(inv_graph, w)
    # print(v.name, w.name)
    print([(item.name, depth) for (item, depth) in Lv])
    print([(item.name, depth) for (item, depth) in Lw])

    # 求交集（可以优化的点，并查集，我现在是O(n2)）
    # 创建字典：节点1的节点与条数
    cnt = dict()
    for item, depth in Lv:
        cnt[item.name] = depth

    # 留下节点2也有的
    uni = [True] * len(cnt.keys())
    for j, (item, depth) in enumerate(Lw):
        if item.name in cnt.keys():
            cnt[item.name] += depth
            for k, it in enumerate(Lv):
                if it[0] == item.name:
                    uni[k] = False
            # uni[j] = False
    # 删去节点2没有的，得到交集
    for j in range(len(uni)):
        if uni[j]:
            del cnt[Lv[j][0].name]

    # 根据跳数排序，
    cnt = sorted(cnt.items(), key=lambda s:s[1])

    # # find nearest common ancestors:
    # for j, (item, depth) in enumerate(Lw):
    #     if item.name in cnt.keys():
    #         return Lv[j]

    # find all common ancestors:
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
    res = find_all_ca(graph=G, v=Vertex(5, "S"), w=Vertex(4, "A1"))
    for item in res:
        print(item)
    # inv_g = G.reverse_graph()
    # inv_g.print_edges()
