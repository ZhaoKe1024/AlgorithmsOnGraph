#!/user/zhao/miniconda3/envs/torch-0
# -*- coding: utf_8 -*-
# @Time : 2023/11/6 20:22
# @Author: ZhaoKe
# @File : ActivityGraph.py
# @Software: PyCharm
""" AOE network
# 一种有向无环图，用有向边表示活动，顶点表示状态
# 求解关键路径(工程最短时间)
# 求解最早、最迟发生时间
# 工程至少需要多长时间？
# 哪些活动需要加快，方能缩短工期？
# 概念参考 https://blog.csdn.net/fangfanglovezhou/article/details/125230610

# # # AOV network
# 顶点表示事件活动，顶点记录时间
# 拓扑排序
"""
import random
from collections import deque
from copy import copy

"""
关键路径求解，关键是求解每个活动的“最早开始时间”和“最晚开始时间”，两者相等就代表是关键活动
"""


class ActivityNetwork(object):
    """同时具有AOV和AOE的性质
    下一步改进，"""

    def __init__(self, vertex_list, edges):
        self.vertex_list = vertex_list

        self.__in_degree_list = [0 for _ in range(len(vertex_list))]
        self.__out_degree_list = [0 for _ in range(len(vertex_list))]

        self.pre_weight = [[] for _ in vertex_list]
        self.post_weight = [[] for _ in vertex_list]

        self.pre_list = [[] for _ in self.vertex_list]
        self.post_list = [[] for _ in vertex_list]

        for edge in edges:
            self.__in_degree_list[edge.post_v] += 1
            self.__out_degree_list[edge.pre_v] += 1
            self.pre_list[edge.post_v].append(vertex_list[edge.pre_v])
            self.post_list[edge.pre_v].append(vertex_list[edge.post_v])
            self.pre_weight[edge.post_v].append(edge.weight)
            self.post_weight[edge.pre_v].append(edge.weight)

        self.marked = [False for _ in range(len(vertex_list))]
        self.topological_set = []

    # 返回一个拓扑序列
    def topological_sort_rand(self):
        que = list()
        V = len(self.vertex_list)
        in_degree_list = copy(self.__in_degree_list)
        marked = [False for _ in self.vertex_list]
        # print("count of vertex:", V)
        for i in range(V):
            if in_degree_list[i] == 0:
                que.append(self.vertex_list[i])
                marked[i] = True
        res = []
        while len(que) > 0:
            ri = random.randint(0, len(que)-1)
            v = que[ri]
            que.pop(ri)
            # print(v)
            res.append(v)
            ind = v.index
            for ver in self.post_list[ind]:
                in_degree_list[ver.index] -= 1
            for i in range(V):
                if in_degree_list[i] == 0 and not marked[i]:
                    que.append(self.vertex_list[i])
                    marked[i] = True
        return res

    """
    按照拓扑序
    从源点出发计算最早发生时间
    从汇点出发计算最晚发生时间
    两个时间相等的就是关键路径
    """

    def critical_path(self):
        v_num = len(self.vertex_list)

        in_degree = self.__in_degree_list.copy()
        out_degree = self.__out_degree_list.copy()
        earlist = [0 for _ in range(v_num)]
        for i in range(v_num):
            if in_degree[i] > 0:
                continue
            dag_j = self.post_list[i]
            for j in range(len(dag_j)):
                temp_value = earlist[i] + self.post_weight[i][j]
                if earlist[dag_j[j].index] < temp_value:
                    earlist[dag_j[j].index] = temp_value
                in_degree[dag_j[j].index] -= 1

        lastlist = [earlist[-1] for _ in range(v_num)]

        for i in range(v_num - 1, -1, -1):
            if out_degree[i] > 0:
                continue
            dag_j = self.pre_list[i]
            for j in range(len(dag_j)):
                temp_value = lastlist[i] - self.pre_weight[i][j]
                if lastlist[dag_j[j].index] > temp_value:
                    lastlist[dag_j[j].index] = temp_value
                out_degree[dag_j[j].index] -= 1

        res_path = []
        for i in range(v_num):
            if earlist[i] == lastlist[i]:
                res_path.append(i)
        # print(res_path)
        return res_path

    # 返回一个拓扑序列
    def topological_sort_all(self):
        self.topological_sort(deque())
        return self.topological_set

    def topological_sort(self, topo_vec):
        if len(topo_vec) == len(self.vertex_list):
            # print(topo_vec)
            # topo_vec.append(vertex)
            # print("here", self.vertex_list[i])
            # print(self.__in_degree_list)
            # print("result:", [ver_1.index for ver_1 in topo_vec])
            for v in list(topo_vec):
                print(v.index, end=' ')
            print()
            # print(list(topo_vec))
            self.topological_set.append(list(topo_vec.copy()))
            # self.topological_set.append([ver_1.index for ver_1 in topo_vec])
            # return
        for i in range(len(self.vertex_list)):
            if self.__in_degree_list[i] == 0 and not self.marked[i]:
                self.marked[i] = True
                topo_vec.append(self.vertex_list[i])
                # print("push", [ver_1.index for ver_1 in topo_vec])
                self.__traverse_apply(self.vertex_list[i].index, False)

                self.topological_sort(topo_vec)

                self.__traverse_apply(self.vertex_list[i].index, True)
                topo_vec.pop()
                # print("pop", [ver_1.index for ver_1 in topo_vec])
                self.marked[i] = False

    def __traverse_apply(self, ind, add_or_sub=False):
        for ver in self.post_list[ind]:
            if add_or_sub:
                self.__in_degree_list[ver.index] += 1
            else:
                self.__in_degree_list[ver.index] -= 1

    # 判断序列是不是该图的拓扑序列
    def check_path(self, path):
        assert len(path) == len(self.vertex_list), "length not matches."
        path_r = path[::-1]
        for i in range(len(path)):
            tmp = [ver.index for ver in self.post_list[path_r[i]]]
            for j in range(len(path) - i - 1):
                if self.vertex_list[path[j]].index in tmp:
                    return False
        return True

class SortedList(object):
    def __init__(self):
        self.sorted_list = []

    def insert_v(self, v):
        if len(self.sorted_list) == 0:
            self.sorted_list.append(v)
            return
        if v.start_time >= self.sorted_list[-1].start_time:
            if self.sorted_list[-1] == v:
                return
            self.sorted_list.append(v)

        list_len = len(self.sorted_list)
        for j in range(list_len-1, -1, -1):
            if j == 0:
                if self.sorted_list[0] == v:
                    return
                self.sorted_list.insert(0, v)
            if v.start_time < self.sorted_list[j].start_time:
                if self.sorted_list[j-1] == v:
                    return
                self.sorted_list.insert(j-1, v)
        print(f"insert successfully: {v.name}")

    def popleft(self):
        v_to_return = self.sorted_list[0]
        self.sorted_list.pop(0)
        return v_to_return

    def __len__(self):
        return len(self.sorted_list)

    def __str__(self):
        return ", ".join([v.name for v in self.sorted_list])


class ConjunctiveGraph(object):
    """同时具有AOV和AOE的性质
    下一步改进，"""

    def __init__(self, vertex_list, opes_num_list, opes_bias_list, mac_num):
        self.vertices = vertex_list
        self.opes_num_list = opes_num_list
        self.opes_bias_list = opes_bias_list
        self.mac_num = mac_num

    def insert_new_operation(self, jid, oid, proc_time, position):
        """
        :param jid: insert operation of jid
        :param oid: and oid
        :param proc_time: with processing time proc_time
        :param position: into position
        :return:
        """
        posi_v = self.vertices[position]
        if oid == 0:
            RS_time = proc_time - posi_v.pre_idle_time
        else:
            now_idle_time = posi_v.start_time - self.vertices[posi_v.in_mac_pre].end_time
            RS_time = proc_time - now_idle_time
        if RS_time < 1e-6:
            print("写一段代码，类似于单链表插入操作")
        else:
            print("开始递归地右移，或者整体右移，分析利弊")

    def get_post_v_tree_list(self, position, proc_time):
        dque = SortedList()
        cur_v = self.vertices[position]
        dque.insert_v(cur_v)
        res_list = [cur_v]
        # print(cur_v)
        while len(dque) > 0:
            cur_v = dque.popleft()
            if cur_v not in res_list:
                res_list.append(cur_v)
            v_j, v_m = None, None
            if cur_v.in_job_post > -1:
                v_j = self.vertices[cur_v.in_job_post]
            if cur_v.in_mac_post > -1:
                v_m = self.vertices[cur_v.in_mac_post]
            if v_j is not None:
                # if v_j not in res_list:
                #     res_list.append(v_j)
                dque.insert_v(v_j)
                # print(f"{cur_v.name} post: injob {v_j.name}")
            if v_m is not None:
                dque.insert_v(v_m)
                # print(f"{cur_v.name} post: inmac {v_m.name}")
            # if v_m is not None:
                # print(f"{cur_v.name} post: inmac {v_m.name}")
            # print(f"{cur_v.name} post: injob {v_j.name}")
            # print("--->next ----")
        # print(dque)
        print("end")
        for res_v in res_list:
            print(res_v)


