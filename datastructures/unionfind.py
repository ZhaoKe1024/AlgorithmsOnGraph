#!/user/zhao/miniconda3/envs/torch-0
# -*- coding: utf_8 -*-
# @Time : 2024/4/10 9:08
# @Author: ZhaoKe
# @File : unionfind.py
# @Software: PyCharm

class UnionFind(object):
    def __init__(self, vertex_list):
        self.parent = []
        self.rank = []
        # self.fa = []
        for i, ver in enumerate(vertex_list):
            # self.fa.append(i)
            self.parent.append(ver.index)
            self.rank.append(1)

    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

    def find(self, idx: int):
        """找到idx的根节点"""
        if self.parent[idx] != idx:
            self.parent[idx] = self.find(self.parent[idx])
            return self.parent[idx]
        return idx

    def connect(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
