
---

### `modulo1-uniform-cost/uniform_cost.py`
```python
import heapq

def uniform_cost_search(graph, start, goal):
    pq = [(0, start, [])]  # (custo, nó, caminho)
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        path = path + [node]

        if node == goal:
            return path, cost

        for neighbor, edge_cost in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(pq, (cost + edge_cost, neighbor, path))
    return None, float("inf")

if __name__ == "__main__":
    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("D", 2), ("E", 5)],
        "C": [("F", 3)],
        "D": [("G", 2)],
        "E": [("G", 1)],
        "F": [("G", 2)],
        "G": []
    }

    path, cost = uniform_cost_search(graph, "A", "G")
    print("Caminho encontrado:", path)
    print("Custo total:", cost)

