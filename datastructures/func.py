#!/user/zhao/miniconda3/envs/torch-0
# -*- coding: utf_8 -*-
# @Time : 2024/4/3 14:05
# @Author: ZhaoKe
# @File : func.py
# @Software: PyCharm
from datastructures.graph_entities import Vertex
from typing import List


def insert_vertex_sorted(array: List[Vertex], key: Vertex) -> int:
    i, L = 0, len(array)
    if L == 0 or key.index > array[-1].index:
        array.append(key)
        return False
    pos = -1
    while i < L:
        if key.index > array[i].index:
            i += 1
        elif key.index == array[i].index:
            return i
        else:
            array.insert(i, key)
            pos = i
            break
    return pos


def print_array(array: List) -> None:
    print("[", end='')
    for item in array:
        print(item, end=', ')
    print("]")


def print_matrix(matrix: List[List]) -> None:
    M, N = len(matrix), len(matrix[0])
    print("----"*N)
    for i in range(M):
        print(matrix[i])
    print("----"*N)

