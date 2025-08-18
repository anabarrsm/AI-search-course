import heapq

def a_star(graph, start, goal, heuristic):
    pq = [(heuristic[start], 0, start, [])]  # (f = g+h, g, nó, caminho)
    visited = set()

    while pq:
        f, g, node, path = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        path = path + [node]

        if node == goal:
            return path, g

        for neighbor, cost in graph.get(node, []):
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(pq, (new_f, new_g, neighbor, path))
    return None, float("inf")

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

    path, cost = a_star(graph, "A", "G", heuristic)
    print("Caminho encontrado:", path)
    print("Custo total:", cost)

