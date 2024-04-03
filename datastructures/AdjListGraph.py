#!/user/zhao/miniconda3/envs/torch-0
# -*- coding: utf_8 -*-
# @Time : 2024/4/3 14:03
# @Author: ZhaoKe
# @File : AdjListGraph.py
# @Software: PyCharm
from datastructures.func import insert_vertex_sorted
from datastructures.graph_entities import Vertex, Edge


class AdjListGraph(object):
    def __init__(self, num_ver: int):
        self.vertices = [Vertex(index=i, name=str(i)) for i in range(num_ver)]
        self.edge_list = []
        self.children = [[] for _ in range(num_ver)]

    def add_vertex(self, key: Vertex):
        insert_vertex_sorted(self.vertices, key=key)

    def add_edge(self, edge: Edge):
        self.edge_list.append(edge)
        insert_vertex_sorted(array=self.children[edge.pre_v], key=self.vertices[edge.post_v])

    def print_edges(self) -> None:
        print(f"=======AdjList_Graph=======")
        for i in range(len(self.vertices)):
            print(self.vertices[i].name, end=': [')
            for ver in self.children[i]:
                print(ver.name, end=', ')
            print("]")

    def reverse_graph(self):
        rev_graph = AdjListGraph(num_ver=len(self.vertices))
        for edge in self.edge_list:
            insert_vertex_sorted(array=rev_graph.children[edge.post_v], key=self.vertices[edge.pre_v])
        return rev_graph

    def __len__(self):
        return len(self.vertices)


class AdjMatrixGraph(object):
    def __init__(self, num_ver):
        self.vertices = [None] * num_ver
        self.adj_matrix = [[-1] * num_ver for _ in range(num_ver)]
        # self.adj_matrix = [[-1] * num_ver] * num_ver  # 我被这一行代码害惨了，直接乘会导致全部都一样

    def add_vertex(self, key):
        pos = insert_vertex_sorted(self.vertices, key=key)
        if pos == -1:
            return
        for i in range(len(self.adj_matrix)):
            self.adj_matrix[i].append(-1)
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)-1, pos-2, -1):
                self.adj_matrix[i][j] = self.adj_matrix[i][j-1]
            self.adj_matrix[i][i] = 0
        self.adj_matrix.insert(pos, [])

    def add_edge_elems(self, pre, post, weight):
        self.adj_matrix[pre][post] = weight

    def add_edge(self, edge: Edge):
        # print("==>", self.adj_matrix[edge.pre_v][edge.post_v])
        # print(f"{edge.pre_v} -> {edge.post_v} : {edge.weight}")
        self.adj_matrix[edge.pre_v][edge.post_v] = edge.weight

    def print_edges(self):
        for row in self.adj_matrix:
            print(row)

    def reverse_graph(self):
        AdjMatrixGraph()

# if __name__ == '__main__':
#     arr = [1,4,6,7,8,5,3]
#     for i in range(7-1, 4-2, -1):
#         print(arr[i])
