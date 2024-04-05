# -*- coding: utf-8 -*-
# @Author : ZhaoKe
# @Time : 2024-04-03 22:08
from typing import List

from datastructures.LayerGraph import LayerNetworkGraph
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


def get_layer_graph_1() -> LayerNetworkGraph:
    """一共有多少层，找深度就够了"""
    return generate_layer_graph(
        name_layer=[["A3"], ["T", "A2"], ["B", "A1"], ["S"], ["D"], ["X"],
                    ],
        edge_layer=[[0, 1], [1, 3], [0, 4], [2, 3], [2, 4], [3, 5], [4, 5], [4, 6], [5, 6], [5, 7], [6, 7]]
    )

def getdg_1():
    # 有向有环图
    return generate_graph(name_list=["R", "B", "C", "A", "D", "E", "F", "F",
                                     "G", "H", "I", "J", "K", "L"],
                          edge_list=[[0, 1], [0,2],[0,3],
                                     [1, 4],
                                     [2, 1], [2, 4], [2,5],
                                     [3, 6], [3,7],
                                     [4, 12],
                                     [5, 8],
                                     [6, 9],
                                     [7, 9],[7, 10],
                                     [8, 5], [8,11],[9,11], [10, 9], [11, 0], [11, 9], [12, 8]])


def generate_layer_graph(name_layer, edge_layer):
    vertex_layer = []
    vertex_list = []
    ind = 0
    for layer in name_layer:
        layer_list = []
        for item in layer:
            vertex_list.append(Vertex(index=ind, name=item))
            layer_list.append(ind)
            ind += 1
        vertex_layer.append(layer_list)
    graph = LayerNetworkGraph(vertex_list=vertex_list, layer_map=vertex_layer)
    for j, edge in enumerate(edge_layer):
        graph.add_edge(Edge(edge_id=j, pre=edge[0], post=edge[1], weight=1))
    return graph


if __name__ == '__main__':
    graph1 = get_layer_graph_1()
    print(graph1.layer_map)
    graph1 = graph1.reverse_graph()
    print(graph1.layer_map)
    graph1.print_edges()
