from collections import defaultdict
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)

        for x, y in connections:
            adj[x].append((y, 1))
            adj[y].append((x, 0))

        visited = [False] * n

        def dfs(node: int, count: int = 0) -> int:
            visited[node] = True
            for next_node, direction in adj[node]:
                if not visited[next_node]:
                    count += direction + dfs(next_node)
            return count

        return dfs(0)


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)

        for x, y in connections:
            adj[x].append((y, 1))
            adj[y].append((x, 0))

        def dfs(node: int, prev_node=None, count: int = 0) -> int:
            for next_node, direction in adj[node]:
                if next_node != prev_node:
                    count += direction + dfs(next_node, node)
            return count

        return dfs(0)


n = 6
connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
print(Solution().minReorder(n, connections))
