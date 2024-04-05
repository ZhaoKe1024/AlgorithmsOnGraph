# -*- coding: utf-8 -*-
# @Author : ZhaoKe
# @Time : 2024-04-05 12:23
from typing import List


class UnDirectedGraph(object):
    def __init__(self, num_ver: int, adj_matrix: List[List]):
        # self.vertex_list = []
        # self.edge_list = []
        self.num_ver = num_ver
        self.adj_matrix = adj_matrix

    def _dfs(self, cur, parent, dfn, low, order, aps):
        """
        reference: https://www.cnblogs.com/YWT-Real/p/16992625.html
        :param cur: 当前遍历到的节点
        :param parent: 当前节点的父节点
        :param dfn: 遍历到的次序
        :param low:
        :param order:
        :param aps: 储存割点的集合
        :return:
        """
        # 当前节点的子树数量
        children = 0
        dfn[cur] = low[cur] = order+1
        order += 1
        for neighbor in self.adj_matrix[cur]:
            if dfn[neighbor] == 0:
                children += 1
                self._dfs(neighbor, cur, dfn, low, order, aps)
                low[cur] = min(low[cur], low[neighbor])
                if (dfn[cur] == 1 and children > 1) or (1 < dfn[cur] <= low[neighbor]):
                    aps.add(cur)
            elif neighbor != parent:
                low[cur] = min(low[cur], dfn[neighbor])

    def find_AP(self):
        # tarjan algorithm
        # 未被访问过的节点的dfn和low初始化为0
        dfn, low = [0]*self.num_ver, [0]*self.num_ver
        order = 0
        aps = set()
        root = 0
        self._dfs(root, -1, dfn, low, order, aps)
        return aps
