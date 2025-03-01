from tabulate import tabulate


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}

        def helper(i, j):
            if i > j:
                return 0

            if i == j:
                return 1

            if (i, j) in memo:
                return memo[(i, j)]
            max_size = 0
            if s[i] == s[j]:
                max_size = helper(i + 1, j - 1) + 2
            else:
                max_size = max(helper(i, j - 1), helper(i + 1, j))
            memo[(i, j)] = max_size

            return memo[(i, j)]

        return helper(0, len(s) - 1)


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        t = s[::-1]
        N = len(s)
        dp = [[0] * (N + 1) for _ in range(N + 1)]

        for i in range(1, N + 1):
            dp[i][i] = 1
            for j in range(1, N + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[N][N]


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        dp = [[0] * (N) for _ in range(N)]

        for i in range(N - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, N):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
            # print(tabulate(dp))
        return dp[0][N - 1]


s = "bbbab"
print(Solution().longestPalindromeSubseq(s))
