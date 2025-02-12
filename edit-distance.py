class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N = len(word1)
        M = len(word2)

        dp = [[0] * (M + 1) for _ in range(N + 1)]

        # base case when w2 is empty
        for i in range(1, N + 1):
            dp[i][0] = i

        # base case when w1 is empty
        for i in range(1, M + 1):
            dp[0][i] = i

        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # replace, delete, insert
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]


word1 = "horse"
word2 = "ros"

print(Solution().minDistance(word1, word2))
