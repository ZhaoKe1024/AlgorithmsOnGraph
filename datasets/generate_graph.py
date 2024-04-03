# -*- coding: utf-8 -*-
# @Author : ZhaoKe
# @Time : 2024-04-03 22:08
from typing import List
from datastructures.graph_entities import Vertex, Edge
from datastructures.AdjListGraph import AdjListGraph


def get_graph_1() -> AdjListGraph:
    return generate_graph(name_list=["H", "O", "P", "Q", "S", "M", "K", "L", "X"],
                          edge_list=[[0, 2], [0, 3], [1, 2], [1, 3], [2, 4], [3, 4], [4, 6], [4, 7], [5, 6], [5, 7],
                                     [6, 8], [7, 8]])


def get_graph_2() -> AdjListGraph:
    return generate_graph(name_list=["A3", "T", "A2", "B", "A1", "S", "D", "X"],
                          edge_list=[[0, 1], [1, 3], [0, 4], [2, 3], [2, 4], [3, 5], [4, 5], [4, 6], [5, 6],
                                     [6, 7], [5, 7]])


def generate_graph(name_list: List[str], edge_list: List[List]) -> AdjListGraph:
    vertices = []
    for i, name in enumerate(name_list):
        vertices.append(Vertex(index=i, name=name))
    graph = AdjListGraph(vertices=vertices)
    for j, edge in enumerate(edge_list):
        graph.add_edge(Edge(edge_id=j, pre=edge[0], post=edge[1], weight=1))
    return graph


if __name__ == '__main__':
    graph1 = get_graph_2()
    graph1.print_edges()
