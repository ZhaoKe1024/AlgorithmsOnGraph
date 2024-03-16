
### Optimization on Graph
It mainly optimizes tasks on a Directed Acyclic Graph (DAG), and the most commonly used graph structure is task scheduling.
- ./GraphAlgorithm.py
- ./datastructure/ActivityGraph.py : Implementation of AOE and AOV(Activity on Vertex).
- ./datasets/graph_example/*.txt

### Topological Sorting
ActivityGraph.py : Implementing the AOV(Activity on Vertex) and AOE(Activity on Edge) Graph Model, and provides follow functions:
- AOV.topological_sort_all(self): Topological sorting of the graph.
- AOV.check_path(self, path)：determining whether a given array is a topological order (subsequence not implemented yet).
- AOE.critical_path(self): find the critical path on this AOE Graph.


``` python ./GraphAlgorithm.py ```

