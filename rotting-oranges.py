from typing import List
from collections import deque


class Solution:
    EMPTY_CELL = 0
    FRESH_ORANGE = 1
    ROTTEN_ORANGE = 2

    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def orangesRotting(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        fresh_oranges: int = 0
        que = deque()

        for i in range(N):
            for j in range(M):
                if grid[i][j] == self.FRESH_ORANGE:
                    fresh_oranges += 1

                if grid[i][j] == self.ROTTEN_ORANGE:
                    que.append((i, j))

        if fresh_oranges == 0:
            return 0

        if not que:
            return -1

        time_taken = -1
        while que:
            time_taken += 1
            for _ in range(len(que)):
                cx, cy = que.popleft()
                for dx, dy in self.DIRECTIONS:
                    nx, ny = cx + dx, cy + dy
                    if (
                        0 <= nx < N
                        and 0 <= ny < M
                        and grid[nx][ny] == self.FRESH_ORANGE
                    ):
                        grid[nx][ny] = self.ROTTEN_ORANGE
                        fresh_oranges -= 1
                        que.append((nx, ny))

        return time_taken if fresh_oranges == 0 else -1


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
# grid = [[0]]
print(Solution().orangesRotting(grid))
