#!/user/zhao/miniconda3/envs/torch-0
# -*- coding: utf_8 -*-
# @Time : 2023/11/6 11:40
# @Author: ZhaoKe
# @File : graph_entities.py
# @Software: PyCharm
import numpy as np


class Vertex(object):
    def __init__(self, index, name, duration=None):
        self.index = index
        self.name = name
        self.in_job_pre = -1
        self.in_mac_pre = -1
        self.in_job_post = -1
        self.in_mac_post = -1
        # vertex as activity
        self.pre_idle_time = 0.
        self.start_time = 0.
        self.end_time = 0.
        self.duration = duration
        self.job_in_degree = 0
        self.job_out_degree = 0

    def __str__(self):
        return f"[{self.index}]:{self.name}, time[{self.start_time},{self.end_time}], pre_idle:{self.pre_idle_time}, params({self.in_job_pre},{self.in_job_post},{self.in_mac_pre},{self.in_mac_post})"

    def get_t_info(self):
        return f"({self.name}[{self.start_time},{self.end_time}]"

    def __eq__(self, other):
        return self.index == other.index

    def set_time(self, st, et):
        self.start_time = st
        self.end_time = et
        self.duration = et - st

    def set_pre_post(self, j_pre, j_post, m_pre):
        self.in_job_pre = j_pre
        self.in_job_post = j_post
        self.in_mac_pre = m_pre

    def set_mac_post(self, m_post):
        self.in_mac_post = m_post


class Edge(object):
    def __init__(self, edge_id, pre, post, weight=np.inf):
        self.edge_id = edge_id
        self.pre_v = pre
        self.post_v = post
        self.weight = weight

    def __str__(self):
        return f"{self.pre_v}->{self.post_v}:{self.weight}"

    def __eq__(self, other):
        return self.pre_v == other.pre_v and self.post_v == other.post_v
