# -*- coding: utf-8 -*-
# @Author : ZhaoKe
# @Time : 2024-04-05 12:46
from datasets.generate_graph import get_graph_1
from datastructures.graph_entities import Vertex, Edge
from datastructures.undirectedgraph import UnDirectedGraph
from datastructures.AdjListGraph import AdjListGraph

if __name__ == '__main__':

    G = get_graph_1()
    G = G.reverse_graph()
    G.print_edges()
    print(G.deep)
    G.topoSort()
    # res = find_all_ca(graph=G, v=Vertex(6, "K"), w=Vertex(7, "L"))
    # for item in res:
    #     print(item)

    # udg = UnDirectedGraph(num_ver=7, adj_matrix=[
    #     [1, 2],
    #     [0, 3],
    #     [0, 3],
    #     [1, 2, 4, 5],
    #     [3, 6],
    #     [3, 6],
    #     [4, 5]])
    # cs = udg.find_AP()
    # print(cs)

    # dg = AdjListGraph(vertices=[Vertex], num_ver=8)
    # dg.children = [
    #     [1, 2],
    #     [3],
    #     [3],
    #     [4, 5],
    #     [6, 7],
    #     [6, 7],
    #     [],
    #     []]
    # cs = dg.topoSort()
    # print(cs)
