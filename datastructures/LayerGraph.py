# -*- coding: utf-8 -*-
# @Author : ZhaoKe
# @Time : 2024-04-04 8:45
# Neural Network Layer wish Graph
# 每一层的节点之间无边，层与层之间单向连接
from typing import List

from datastructures.func import insert_vertex_sorted
from datastructures.graph_entities import Edge


class LayerNetworkGraph(object):
    def __init__(self, num_ver: int, vertex_layer: List[List], children: List[List]):
        self.vertex_layer = vertex_layer
        self.num_ver = num_ver
        self.vertex_list = []
        for layer in vertex_layer:
            self.vertex_list.extend(layer)
        self.indegree = [0] * self.num_ver
        self.outdegree = [0] * self.num_ver
        self.edge_list = []
        if children:
            self.children = children
            for i, child_list in enumerate(children):
                self.outdegree[i] = len(child_list)
                # print(child_list)
                for child in child_list:
                    self.indegree[child] += 1
                    self.edge_list.append([i, child])
        else:
            self.children = [[] for _ in range(self.num_ver)]
        # print(self.edge_list)
        
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
        # Depth = 0
        Depth = len(self.vertex_layer)
        new_vertex_layer = [self.vertex_layer[Depth-1-i] for i in range(Depth)]
        new_children = [[] for _ in range(self.num_ver)]
        for i, child_list in enumerate(self.children):
            for child in child_list:
                new_children[child].append(i)
        rev_graph = LayerNetworkGraph(num_ver=self.num_ver,
                        vertex_layer=new_vertex_layer, children=new_children)
        return rev_graph

    def print_children(self):
        print("====children====")
        for ver_list in self.vertex_layer:
            print([item.name for item in ver_list])
            # print("[", end='')
            for ver in ver_list:
                print(ver.name, ":", self.children[ver.index])
                # print(ver.name, ":", [self.vertex_list[idx].name for idx in self.children[ver.index]])  # , end=',')
            # print("]")
