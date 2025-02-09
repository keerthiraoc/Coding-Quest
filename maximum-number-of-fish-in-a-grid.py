from typing import List
from collections import deque


class Solution:
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def calculate_fishes(self, x, y, grid, visited):
        if (
            x < 0
            or x >= len(grid)
            or y < 0
            or y >= len(grid[0])
            or grid[x][y] == 0
            or visited[x][y]
        ):
            return 0

        visited[x][y] = True
        fishes_count = grid[x][y]
        for dx, dy in self.DIRECTIONS:
            nx, ny = x + dx, y + dy
            fishes_count += self.calculate_fishes(nx, ny, grid, visited)
        return fishes_count

    def findMaxFish(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        max_fishes_count = 0

        visited = [[False] * M for _ in range(N)]

        for i in range(N):
            for j in range(M):
                if grid[i][j] > 0 and not visited[i][j]:
                    max_fishes_count = max(
                        max_fishes_count, self.calculate_fishes(i, j, grid, visited)
                    )

        return max_fishes_count


class Solution:
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def calculate_fishes(self, x, y, grid, visited):
        que = deque()
        que.append((x, y))

        fishes_count = 0
        while len(que) > 0:
            cx, cy = que.popleft()
            if visited[cx][cy]:
                continue
            visited[cx][cy] = True
            fishes_count += grid[cx][cy]

            for dx, dy in self.DIRECTIONS:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] > 0:
                    que.append((nx, ny))
        return fishes_count

    def findMaxFish(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        max_fishes_count = 0

        visited = [[False] * M for _ in range(N)]

        for i in range(N):
            for j in range(M):
                if grid[i][j] > 0 and not visited[i][j]:
                    max_fishes_count = max(
                        max_fishes_count, self.calculate_fishes(i, j, grid, visited)
                    )

        return max_fishes_count


grid = [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]
grid = [[8, 6], [2, 6]]
print(Solution().findMaxFish(grid))
