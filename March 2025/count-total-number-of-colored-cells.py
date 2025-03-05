class Solution:
    def coloredCells(self, n: int) -> int:
        colored_cells = 1
        for i in range(1, n):
            colored_cells += 4 * i

        return colored_cells


class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + n * (n - 1) * 2


n = 5
print(Solution().coloredCells(n))
