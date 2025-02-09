from typing import List


class Solution:
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def _dfs(self, x, y, grid, visited, idx):
        if (
            x < 0
            or x >= len(grid)
            or y < 0
            or y >= len(grid[0])
            or grid[x][y] != 1
            or visited[x][y]
        ):
            return 0

        visited[x][y] = True
        grid[x][y] = idx
        count = 1
        for dx, dy in self.DIRECTIONS:
            nx, ny = x + dx, y + dy
            count += self._dfs(nx, ny, grid, visited, idx)

        return count

    def largestIsland(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        visited = [[False] * M for _ in range(N)]

        idx = 2
        island_mapping = {}
        for i in range(N):
            for j in range(M):
                if not visited[i][j] and grid[i][j] == 1:
                    island_mapping[idx] = self._dfs(i, j, grid, visited, idx)
                    idx += 1

        if not island_mapping:
            return 1

        if len(island_mapping) == 1:
            return (
                island_mapping[idx - 1]
                if N * M == island_mapping[idx - 1]
                else island_mapping[idx - 1] + 1
            )

        max_count = 0
        for i in range(N):
            for j in range(M):

                if grid[i][j] == 0:
                    grid_count = {}

                    for dx, dy in self.DIRECTIONS:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] != 0:
                            grid_count[grid[nx][ny]] = island_mapping[grid[nx][ny]]

                    max_count = max(max_count, sum(grid_count.values()))

        return max_count + 1


grid = [
    [0, 0, 0, 1, 1],
    [1, 0, 0, 1, 0],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 1, 0],
]
print(Solution().largestIsland(grid))
