from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        adj = defaultdict(dict)
        for i in range(len(equations)):
            num, den = equations[i]
            quo = values[i]
            adj[num][den] = quo
            adj[den][num] = 1.0 / quo

        def dfs(src, dest, visited, ans, temp):
            if src in visited:
                return

            visited.add(src)
            if src == dest:
                ans[0] = temp
                return

            for x, y in adj[src].items():
                dfs(x, dest, visited, ans, temp * y)

        res = []
        for num, den in queries:
            if num not in adj or den not in adj:
                res.append(-1.0)
            else:
                visited = set()
                ans = [-1.0]
                temp = 1.0
                dfs(num, den, visited, ans, temp)
                res.append(ans[0])

        return res


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

print(Solution().calcEquation(equations, values, queries))
