from typing import List
from collections import defaultdict


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        N = len(queries)
        res = []
        color_map = {}
        ball_map = {}

        for i in range(N):
            ball, color = queries[i]

            if ball in ball_map:
                prev_color = ball_map[ball]
                color_map[prev_color] -= 1

                if color_map[prev_color] == 0:
                    del color_map[prev_color]

            ball_map[ball] = color
            color_map[color] = color_map.get(color, 0) + 1
            res.append(len(color_map))

        return res


limit = 4
queries = [[1, 4], [2, 5], [1, 3], [3, 4]]

print(Solution().queryResults(limit, queries))
