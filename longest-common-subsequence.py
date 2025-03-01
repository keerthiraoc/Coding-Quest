class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == text2:
            return len(text1)

        N, M = len(text1), len(text2)
        memo = {}

        def helper(i, j):
            if i >= N or j >= M:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            max_size = 0
            if text1[i] == text2[j]:
                max_size = helper(i + 1, j + 1) + 1
            else:
                max_size = max(helper(i + 1, j), helper(i, j + 1))
            memo[(i, j)] = max_size

            return memo[(i, j)]

        return helper(0, 0)


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N, M = len(text1), len(text2)
        dp = [[0] * (M + 1) for _ in range(N + 1)]

        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[N][M]


text2 = "abcde"
text1 = "ace"

text1 = "pmjghexybyrgzczy"
text2 = "hafcdqbgncrcbihkd"

print(Solution().longestCommonSubsequence(text1, text2))
