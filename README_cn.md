
## 1 Graph Model
- Vertec and Edge: ./datastructure/graph_entities.py
- Directed Graph: ./datastructure/AdjListGraph/AdjListGraph
- Undirected Graph: ./datastructure/undirectedgraph/UnDirectedGraph

## 2 图上的算法

### 2.1 拓扑排序和关键路径
主要关注有向无环图, 以及最常见的数据结构和算法例如关键路径、拓扑排序。
- 运行算法./GraphAlgorithm.py
- 数据结构：./datastructure/ActivityGraph.py : Implementation of AOE and AOV(Activity on Vertex).
- 数据案例：./datasets/graph_example/*.txt

#### run
``` python ./GraphAlgorithm.py ```

#### Topological Sorting
ActivityGraph.py : AOV和AOE模型的实现, 包含以下算法:
- AOV.topological_sort_all(self): Topological sorting of the graph.
- AOV.check_path(self, path)：determining whether a given array is a topological order (subsequence not implemented yet).
- AOE.critical_path(self): find the critical path on this AOE Graph.


### 2.2 最近公共祖先问题
返回所有公共祖先

./CommonAncestors.find_all_ca(graph=G, v=v1, w=v2)

- 数据结构：./datastructures/AdjListGraph.py
- 算法: ./CommonAncestors.py

#### run
```python ./CommonAncestors.py```

### 2.3 所有共同祖先（直到必经点）
定义共同祖先：