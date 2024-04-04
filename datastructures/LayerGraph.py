# -*- coding: utf-8 -*-
# @Author : ZhaoKe
# @Time : 2024-04-04 8:45
# Neural Network Layer wish Graph
# 每一层的节点之间无边，层与层之间单向连接
from typing import List

from datastructures.func import insert_vertex_sorted
from datastructures.graph_entities import Edge


class LayerEdge(object):
    def __init__(self, in_layer, in_index, out_layer, out_index):
        self.in_layer = in_layer
        self.in_index = in_index
        self.out_layer = out_layer
        self.out_index = out_index


class LayerNetworkGraph(object):
    def __init__(self, vertex_list: List, layer_map):
        self.vertex_list = vertex_list
        self.layer_map = layer_map
        self.edge_list = []
        self.children = [[] for _ in range(len(self.vertex_list))]
        self.indegree = [0] * len(self.vertex_list)
        self.outdegree = [0] * len(self.vertex_list)

    def add_edge(self, edge):
        self.edge_list.append(edge)
        insert_vertex_sorted(array=self.children[edge.pre_v], key=self.vertex_list[edge.post_v])
        self.indegree[edge.post_v] += 1
        self.outdegree[edge.pre_v] += 1

    def print_edges(self) -> None:
        print(f"=======AdjList_Graph=======")
        for i in range(len(self.vertex_list)):
            print(self.vertex_list[i].name, end=': [')
            for ver in self.children[i]:
                print(ver.name, end=', ')
            print("]")

    def reverse_graph(self):
        Depth = len(self.layer_map)
        L = len(self.vertex_list)
        new_map = [[L-1-i for i in self.layer_map[Depth-1-i]] for i in range(Depth)]
        rev_graph = LayerNetworkGraph(vertex_list=self.vertex_list, layer_map=new_map)
        for edge in self.edge_list:
            rev_graph.add_edge(Edge(edge.edge_id, pre=edge.post_v, post=edge.pre_v, weight=edge.weight))
        return rev_graph
