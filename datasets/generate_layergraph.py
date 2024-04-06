# -*- coding: utf-8 -*-
# @Author : ZhaoKe
# @Time : 2024-04-06 22:52
from datastructures.graph_entities import Vertex
from datastructures.LayerGraph import LayerNetworkGraph


def get_layergraph_1():
    vertex_list = [Vertex(index=0, name="H"), Vertex(index=1, name="O"),
                   Vertex(index=2, name="P"), Vertex(index=3, name="Q"),
                   Vertex(index=4, name="S"), Vertex(index=5, name="M"),
                   Vertex(index=6, name="K"), Vertex(index=7, name="L"),
                   Vertex(index=8, name="X")]
    vertex_layer = [[0, 1], [2, 3], [4, 5], [6, 7], [8]]
    children_list = [
        [2, 3],
        [2, 3],
        [4], [4],
        [6, 7],
        [6, 7],
        [8], [8]
    ]
    layergraph = LayerNetworkGraph(vertex_list=vertex_list, vertex_layer=vertex_layer, children=children_list)
    return layergraph


def get_instant_1():
    depth = 6
    num_per_layer = [9, 7, 5, 3, 2, 1]
    vertex_list = []
    vertex_layer = [[] for _ in range(depth)]
    idx = 0
    for j, num in enumerate(num_per_layer):
        for i in range(num):
            vertex_list.append(Vertex(index=idx, name=str(j) + '_' + str(i), depth=j))
            vertex_layer[j].append(idx)
            idx += 1
    children_list = [[] for _ in range(len(vertex_list))]
    children_list[0] = [9, 10]
    children_list[1] = [9]
    children_list[2] = [10]
    children_list[3] = [11, 12, 13]
    children_list[4] = [11]
    children_list[5] = [12, 13]
    children_list[6] = [14, 15]
    children_list[7] = [14]
    children_list[8] = [15]
    children_list[9] = [16]
    children_list[10] = [17, 18]
    children_list[11] = [17]
    children_list[12] = [16, 19, 20]
    children_list[13] = [18]
    children_list[14] = [19]
    children_list[15] = [20]
    children_list[16] = [21]
    children_list[17] = [21]
    children_list[18] = [22, 23]
    children_list[19] = [22]
    children_list[20] = [23]
    children_list[21] = [24, 25]
    children_list[22] = [24]
    children_list[23] = [25]
    children_list[24] = [26]
    children_list[25] = [26]
    children_list[26] = []
    layergraph = LayerNetworkGraph(vertex_list=vertex_list, vertex_layer=vertex_layer, children=children_list)
    return layergraph
