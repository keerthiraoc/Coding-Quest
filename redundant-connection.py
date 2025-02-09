from typing import List


class DSU:
    def __init__(self, N):
        self.N = N
        self.size = [1] * N
        self.representation = list(range(N))

    def _find(self, node):
        if self.representation[node] == node:
            return node

        self.representation[node] = self._find(self.representation[node])
        return self.representation[node]

    def _do_union(self, node_one, node_two):
        node_one = self._find(node_one)
        node_two = self._find(node_two)

        if node_one == node_two:
            return False
        else:
            if self.size[node_one] > self.size[node_two]:
                self.representation[node_two] = node_one
                self.size[node_one] += self.size[node_two]
            else:
                self.representation[node_one] = node_two
                self.size[node_two] += self.size[node_one]
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        dsu = DSU(N)
        for edge in edges:
            if not dsu._do_union(edge[0] - 1, edge[1] - 1):
                return edge

        return []


class Solution:
    def _is_connected(self, src, target, adj_list, visited):
        visited[src] = True
        if src == target:
            return True

        is_found = False
        for edge in adj_list[src]:
            if not visited[edge]:
                is_found = is_found or self._is_connected(
                    edge, target, adj_list, visited
                )

        return is_found

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        adj_list = [[] for _ in range(N)]

        for edge in edges:
            visited = [False] * N

            if self._is_connected(edge[0] - 1, edge[1] - 1, adj_list, visited):
                return edge

            adj_list[edge[0] - 1].append(edge[1] - 1)
            adj_list[edge[1] - 1].append(edge[0] - 1)

        return []


class Solution:
    cycle_start = -1

    def _DFS(self, src, visited, adj_list, parent):
        visited[src] = True

        for adj in adj_list[src]:
            if not visited[adj]:
                parent[adj] = src
                self._DFS(adj, visited, adj_list, parent)
            elif adj != parent[src] and self.cycle_start == -1:
                self.cycle_start = adj
                parent[adj] = src

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        adj_list = [[] for _ in range(N)]
        for edge in edges:
            adj_list[edge[0] - 1].append(edge[1] - 1)
            adj_list[edge[1] - 1].append(edge[0] - 1)

        visited = [False] * N
        parent = [-1] * N
        self._DFS(0, visited, adj_list, parent)

        cycle_nodes = {}
        node = self.cycle_start

        while True:
            cycle_nodes[node] = 1
            node = parent[node]
            if node == self.cycle_start:
                break

        for i in range(len(edges) - 1, -1, -1):
            if (edges[i][0] - 1) in cycle_nodes and (edges[i][1] - 1) in cycle_nodes:
                return edges[i]

        return []


edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
print(Solution().findRedundantConnection(edges))
