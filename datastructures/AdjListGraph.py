#!/user/zhao/miniconda3/envs/torch-0
# -*- coding: utf_8 -*-
# @Time : 2024/4/3 14:03
# @Author: ZhaoKe
# @File : AdjListGraph.py
# @Software: PyCharm
from collections import deque
from copy import copy
from typing import List
from datastructures.func import insert_vertex_sorted
from datastructures.graph_entities import Vertex, Edge


class AdjListGraph(object):
    """
    有向图
    """

    def __init__(self, vertices, num_ver: int = 0):
        if vertices:
            self.vertices = vertices
        else:
            self.vertices = [Vertex(index=i, name=str(i)) for i in range(num_ver)]
        self.edge_list = []
        self.children = [[] for _ in range(len(self.vertices))]
        self.indegree = [0] * len(self.vertices)
        self.outdegree = [0] * len(self.vertices)
        L = len(self.vertices)
        self.deep = [0] * L
        self.dp = [[0] * L for _ in range(9)]

    # def __dfs(self, cur, array):
    #     if cur is None:
    #         return
    #     if cur.

    def get_Deep_list(self):
        deep = [0] * len(self.vertices)
        self.__dfs(self.vertices[0], deep)
        print(deep)

    def add_vertex(self, key: Vertex):
        insert_vertex_sorted(self.vertices, key=key)

    def add_edge(self, edge: Edge):
        self.edge_list.append(edge)
        insert_vertex_sorted(array=self.children[edge.pre_v], key=self.vertices[edge.post_v])
        self.indegree[edge.post_v] += 1
        self.outdegree[edge.pre_v] += 1

    def print_edges(self) -> None:
        print(f"=======AdjList_Graph=======")
        for i in range(len(self.vertices)):
            print(self.vertices[i].name, end=': [')
            for ver in self.children[i]:
                print(ver.name, end=', ')
            print("]")

    def reverse_graph(self):
        rev_graph = AdjListGraph(vertices=self.vertices, num_ver=len(self.vertices))
        for edge in self.edge_list:
            rev_graph.add_edge(Edge(edge.edge_id, pre=edge.post_v, post=edge.pre_v, weight=edge.weight))
        return rev_graph

    def __len__(self):
        return len(self.vertices)

    def topoSort(self) -> List[int]:
        dq = deque()
        L = len(self.vertices)
        in_degree_list = copy(self.indegree)
        for i in range(L):
            if in_degree_list[i] == 0:
                dq.append(i)
        ans, ind = [], 0
        # print("[", end='')
        while len(dq) > 0:
            cur = dq.popleft()
            # print(self.vertices[cur].name, end=", ")
            ans.append(self.vertices[cur].index)
            # now = a[ind].index
            # print(now)
            for i in range(len(self.children[cur])):
                to = self.children[cur][i].index
                in_degree_list[to] -= 1
                if in_degree_list[to] == 0:
                    dq.append(to)
        # print("]")
        return ans
        # print([item.name for item in a])
        # return [item for ]

    def get_LCA(self, x: int, y: int):
        if self.deep[x] < self.deep[y]:
            x, y = y, x
        cnt = self.deep[x] - self.deep[y]
        for i in range(9):
            if (1 << i) & cnt:
                x = self.dp[x][i]
        if x == y:
            return x
        for i in range(9 - 1, -1, -1):
            if self.dp[x][i] != self.dp[y][i]:
                x = self.dp[x][i]
                y = self.dp[y][i]
        return self.dp[x][0]

    def generate_dominated_tree(self):
        Gf = self.reverse_graph()
        a = self.topoSort()
        # deep = [0] * len(self.vertices)
        for i in range(len(self.vertices)):
            x = a[i]
            if len(self.children[x]) == 0:
                self.children[0].append(x)
                self.deep[x] = 1
                continue
            y = self.children[x][0]
            for i in range(len(self.children[x])):
                y = self.get_LCA(y, self.children[x][i])
            self.deep[x] = self.deep[y]+1
            self.dp[x][0] = y
            for i in range(9):
                self.dp[x][i] = self.dp[self.dp[x][i-1]][i-1]


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
            for j in range(len(self.vertices) - 1, pos - 2, -1):
                self.adj_matrix[i][j] = self.adj_matrix[i][j - 1]
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
