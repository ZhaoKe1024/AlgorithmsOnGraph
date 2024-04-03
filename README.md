
## Algorithms on Graph
It mainly optimizes tasks on a Directed Acyclic Graph (DAG), and the most commonly used graph structure is task scheduling, including critical path and topological sorting.
- Run Program: ./GraphAlgorithm.py
- Data Structure: ./datastructure/ActivityGraph.py : Implementation of AOE and AOV(Activity on Vertex).
- Data Example: ./datasets/graph_example/*.txt

### run
``` python ./GraphAlgorithm.py ```

## Topological Sorting
ActivityGraph.py : Implementing the AOV(Activity on Vertex) and AOE(Activity on Edge) Graph Model, and provides follow functions:
- AOV.topological_sort_all(self): Topological sorting of the graph.
- AOV.check_path(self, path)：determining whether a given array is a topological order (subsequence not implemented yet).
- AOE.critical_path(self): find the critical path on this AOE Graph.

## Local Common Ancestor Problem
- data structure：./datastructures/AdjListGraph.py
- algorithm: ./CommonAncestors.py

### run
```python ./CommonAncestors.py```
