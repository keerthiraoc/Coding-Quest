from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        R, C = len(matrix), len(matrix[0])
        ans = [[None] * R for _ in range(C)]
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                ans[c][r] = val

        return ans


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # print(*matrix)
        return list(zip(*matrix))


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution().transpose(matrix))
