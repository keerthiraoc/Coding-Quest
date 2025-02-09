from typing import List
from collections import deque


class Solution:
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        N, M = len(maze), len(maze[0])

        x, y = entrance
        que = deque([(x, y, 0)])
        maze[x][y] = "+"

        while que:
            cx, cy, count = que.popleft()

            for dx, dy in self.DIRECTIONS:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == ".":
                    if (nx == 0 or nx == N - 1) or (ny == 0 or ny == M - 1):
                        return count + 1

                    maze[nx][ny] = "+"
                    que.append((nx, ny, count + 1))

        return -1


maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
entrance = [1, 2]

maze = [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]]
entrance = [1, 0]

maze = [[".", "+"]]
entrance = [0, 0]
print(Solution().nearestExit(maze, entrance))
