# -*- coding: utf-8 -*-
# @Author : ZhaoKe
# @Time : 2023-12-25 22:34
import numpy as np
from datastructures.graph_entities import Vertex
from datastructures.ActivityGraph import ConjunctiveGraph


def read_graph_scheduled(graph_file_path):
    job_set = set()
    with open(graph_file_path, 'r') as fin:
        lines = fin.readlines()

    for line in lines:
        line_parts = line.strip().split('|')
        # print(line_parts)
        for item in line_parts:
            if len(item) < 1:
                continue
            job_set.add(int(item.split('-')[0][1:]))
    job_num = len(job_set)
    opes_num_list = [0 for _ in range(job_num)]
    for line in lines:
        line_parts = line.strip().split('|')
        for item in line_parts:
            if len(item) < 1:
                continue
            jpart = item.split('-')
            jid = int(jpart[0][1:])
            opes_num_list[jid] += 1
    # print("nums:")
    # print(opes_num_list)
    max_opes_num = sum(opes_num_list)
    opes_appertain_list = [-1 for _ in range(max_opes_num)]
    idx = 0
    for j, num in enumerate(opes_num_list):
        for i in range(num):
            opes_appertain_list[idx] = j
            idx += 1
    # print("appertain:")
    # print(opes_appertain_list)
    opes_num_list.insert(0, 0)
    opes_bias_list = np.cumsum(opes_num_list)
    # print("bias:")
    # print(opes_bias_list)
    v_list = [None for _ in range(max_opes_num)]
    idx = 0
    for line in lines:
        line_parts = line.strip().split('|')
        m_pre_id = -1
        for imid, item in enumerate(line_parts):
            if len(item) < 1:
                continue
            jpart = item.split('-')
            jid = int(jpart[0][1:])
            opart = jpart[1].split('[')
            oid = int(opart[0][:-1])
            tpart = opart[1].split(',')
            st = float(tpart[0])
            et = float(tpart[1][:-1])
            # print(f"({jid}-{oid})[{tt},{et}]")
            tmp_v = Vertex(idx, f"({jid}-{oid})")
            tmp_v.set_time(st, et)
            prepost_params = [-1, -1, -1]
            if oid > 0:
                # 有前驱
                prepost_params[0] = opes_bias_list[jid]+oid - 1
            if opes_bias_list[jid]+oid < opes_bias_list[jid+1]-1:
                # if oid <
                # 有后继
                prepost_params[1] = opes_bias_list[jid]+oid + 1
            # if imid == 0:
            #     m_pre_v = tmp_v
            if imid > 0:
                # 有后继
                prepost_params[2] = v_list[m_pre_id].index
                v_list[m_pre_id].set_mac_post(opes_bias_list[jid]+oid)
            tmp_v.set_pre_post(*prepost_params)
            if oid == 0:
                tmp_v.pre_idle_time = 0.
            else:
                if imid == 0:
                    tmp_v.pre_idle_time = st
                else:
                    tmp_v.pre_idle_time = st - v_list[m_pre_id].end_time
            v_list[opes_bias_list[jid]+oid] = tmp_v
            m_pre_id = opes_bias_list[jid]+oid
            idx += 1
    # for v in v_list:
    #     print(v)
    # start_v = v_list[16]
    # while start_v.in_mac_post != -1:
    #     print(start_v)
    #     start_v = v_list[start_v.in_mac_post]
    # print(start_v)

    # while start_v.in_job_post != -1:
    #     print(start_v)
    #     start_v = v_list[start_v.in_job_post]
    # print(start_v)
    return v_list, opes_num_list, opes_bias_list, len(lines)


if __name__ == '__main__':
    ver_set, opes_num_list, opes_bias_list, mac_num = read_graph_scheduled("../fjspkits/results/mk01/t202312260902_planning.txt")
    CG = ConjunctiveGraph(ver_set, opes_num_list, opes_bias_list, mac_num)

    CG.get_post_v_tree_list(16, 3)
