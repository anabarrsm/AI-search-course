import heapq

class EightPuzzle:
    def __init__(self, start_state, goal_state="12345678_"):
        """
        Representa o problema do 8-puzzle.
        Estado é representado como string, ex: "12345678_"
        "_" representa o espaço vazio.
        """
        self.start = start_state
        self.goal = goal_state

    def get_neighbors(self, state):
        """Retorna todos os estados vizinhos possíveis."""
        neighbors = []
        idx = state.index("_")
        row, col = divmod(idx, 3)
        moves = [(-1,0), (1,0), (0,-1), (0,1)]  # cima, baixo, esq, dir

        for dr, dc in moves:
            r, c = row + dr, col + dc
            if 0 <= r < 3 and 0 <= c < 3:
                new_idx = r * 3 + c
                state_list = list(state)
                state_list[idx], state_list[new_idx] = state_list[new_idx], state_list[idx]
                neighbors.append("".join(state_list))
        return neighbors

    def heuristic(self, state):
        """Heurística Manhattan distance."""
        dist = 0
        for i, val in enumerate(state):
            if val == "_":
                continue
            goal_idx = self.goal.index(val)
            r1, c1 = divmod(i, 3)
            r2, c2 = divmod(goal_idx, 3)
            dist += abs(r1 - r2) + abs(c1 - c2)
        return dist

    def solve(self):
        """Resolve usando A* search."""
        frontier = [(self.heuristic(self.start), 0, self.start, [])]
        visited = set()

        while frontier:
            _, cost, state, path = heapq.heappop(frontier)
            if state == self.goal:
                return path + [state]

            if state in visited:
                continue
            visited.add(state)

            for neighbor in self.get_neighbors(state):
                if neighbor not in visited:
                    new_cost = cost + 1
                    priority = new_cost + self.heuristic(neighbor)
                    heapq.heappush(frontier, (priority, new_cost, neighbor, path + [state]))
        return None


if __name__ == "__main__":
    puzzle = EightPuzzle("7245_6831")  # exemplo inicial
    solution = puzzle.solve()
    if solution:
        print("Solução encontrada em", len(solution)-1, "movimentos:")
        for s in solution:
            print(s[0:3])
            print(s[3:6])
            print(s[6:9])
            print()
    else:
        print("Sem solução.")

