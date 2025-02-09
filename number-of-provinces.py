from typing import List


# DFS
class Solution:
    def dfs(self, isConnected, node, visited):
        visited[node] = True
        for i in range(len(isConnected)):
            if isConnected[node][i] == 1 and not visited[i]:
                self.dfs(isConnected, i, visited)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        visited = [False] * N

        provinces = 0
        for i in range(N):
            if not visited[i]:
                provinces += 1
                self.dfs(isConnected, i, visited)

        return provinces


# BFS
class Solution:
    def bfs(self, node, isConnected, visited):
        from collections import deque

        que = deque([node])
        visited[node] = True

        while que:
            curr_node = que.popleft()

            for i in range(len(isConnected)):
                if isConnected[curr_node][i] and not visited[i]:
                    que.append(i)
                    visited[i] = True

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        provinces = 0
        visited = [False] * N

        for i in range(N):
            if not visited[i]:
                provinces += 1
                self.bfs(i, isConnected, visited)

        return provinces


# union find
class UnionFind:
    def __init__(self, size):
        self.rank = [0] * size
        self.parent = list(range(size))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union_set(self, x, y):
        xset = self.find(x)
        yset = self.find(y)

        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        uf = UnionFind(N)
        components = N

        for i in range(N):
            for j in range(i + 1, N):
                if isConnected[i][j] and uf.find(i) != uf.find(j):
                    components -= 1
                    uf.union_set(i, j)
        print(uf.parent, uf.rank)
        return components


# isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(Solution().findCircleNum(isConnected))
