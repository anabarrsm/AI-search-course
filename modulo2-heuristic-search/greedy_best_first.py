import heapq

def greedy_best_first(graph, start, goal, heuristic):
    pq = [(heuristic[start], start, [])]  # (h, nó, caminho)
    visited = set()

    while pq:
        h, node, path = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        path = path + [node]

        if node == goal:
            return path

        for neighbor, cost in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor, path))
    return None

if __name__ == "__main__":
    graph = {
        "A": [("B", 1), ("C", 3)],
        "B": [("D", 1), ("E", 5)],
        "C": [("F", 2)],
        "D": [("G", 4)],
        "E": [("G", 1)],
        "F": [("G", 2)],
        "G": []
    }

    heuristic = {
        "A": 7, "B": 6, "C": 5,
        "D": 4, "E": 2, "F": 1,
        "G": 0
    }

    path = greedy_best_first(graph, "A", "G", heuristic)
    print("Caminho encontrado:", path)

