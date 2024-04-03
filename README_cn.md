
## run
``` python ./GraphAlgorithm.py ```

### 图上的算法
主要关注有向无环图, 以及最常见的数据结构和算法例如关键路径、拓扑排序。
- ./GraphAlgorithm.py
- ./datastructure/ActivityGraph.py : Implementation of AOE and AOV(Activity on Vertex).
- ./datasets/graph_example/*.txt

### Topological Sorting
ActivityGraph.py : AOV和AOE模型的实现, 包含以下算法:
- AOV.topological_sort_all(self): Topological sorting of the graph.
- AOV.check_path(self, path)：determining whether a given array is a topological order (subsequence not implemented yet).
- AOE.critical_path(self): find the critical path on this AOE Graph.


## 公共祖先问题
- 数据结构：./datastructures/AdjListGraph.py
- 算法: ./CommonAncestors.py

### run
```python ./CommonAncestors.py```

