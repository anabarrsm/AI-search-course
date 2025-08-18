from collections import deque

class MazeSolver:
    def __init__(self, maze, start, goal):
        """
        maze: lista de strings (matriz do labirinto)
        start: (linha, coluna)
        goal: (linha, coluna)
        """
        self.maze = maze
        self.start = start
        self.goal = goal
        self.rows = len(maze)
        self.cols = len(maze[0])

    def neighbors(self, r, c):
        """Retorna vizinhos válidos (sem atravessar paredes)."""
        moves = [(-1,0), (1,0), (0,-1), (0,1)]
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols and self.maze[nr][nc] != "#":
                yield nr, nc

    def bfs(self):
        """Resolve com busca em largura (BFS)."""
        queue = deque([(self.start, [self.start])])
        visited = set([self.start])

        while queue:
            (r, c), path = queue.popleft()
            if (r, c) == self.goal:
                return path

            for nr, nc in self.neighbors(r, c):
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), path + [(nr, nc)]))
        return None


if __name__ == "__main__":
    maze = [
        "#########",
        "#S   #  #",
        "# ## # ##",
        "#    #  #",
        "### ##  #",
        "#      G#",
        "#########"
    ]

    start = (1, 1)
    goal = (5, 7)

    solver = MazeSolver(maze, start, goal)
    path = solver.bfs()

    if path:
        print("Caminho encontrado:")
        for step in path:
            print(step)
    else:
        print("Sem caminho possível.")

