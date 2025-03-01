# TLE
# time complexity: O(2^(n + m)) * (n + m)
# space: O(m + n) ^ 2
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1

        if len(str1) == 0 and len(str2) == 0:
            return ""

        if not str1:
            return str2
        elif not str2:
            return str1

        if str1[0] == str2[0]:
            return str1[0] + self.shortestCommonSupersequence(str1[1:], str2[1:])
        else:
            pick_str1 = str1[0] + self.shortestCommonSupersequence(str1[1:], str2)
            pick_str2 = str2[0] + self.shortestCommonSupersequence(str1, str2[1:])

            return pick_str2 if len(pick_str1) > len(pick_str2) else pick_str1


# MLE
# time complexity: O(n*m *(n+m))
# space complexity: O(n*m *(n+m))
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        memo = {}

        def helper(s1, s2):
            if s1 == s2:
                return s1

            if not s1 and not s2:
                return ""

            if not s1:
                return s2
            elif not s2:
                return s1

            if (s1, s2) in memo:
                return memo[(s1, s2)]

            if s1[0] == s2[0]:
                memo[(s1, s2)] = s1[0] + helper(s1[1:], s2[1:])
                return memo[(s1, s2)]
            else:
                pick_s1 = s1[0] + helper(s1[1:], s2)
                pick_s2 = s2[0] + helper(s1, s2[1:])

                memo[(s1, s2)] = pick_s2 if len(pick_s1) > len(pick_s2) else pick_s1
                return memo[(s1, s2)]

        return helper(str1, str2)


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        N, M = len(str1), len(str2)

        prev_row = [str2[0:i] for i in range(M + 1)]

        for row in range(1, N + 1):
            curr_row = [str1[0:row]] + [None for _ in range(M)]

            for col in range(1, M + 1):
                if str1[row - 1] == str2[col - 1]:
                    curr_row[col] = prev_row[col - 1] + str1[row - 1]
                else:
                    pick_s1 = prev_row[col]
                    pick_s2 = curr_row[col - 1]

                    curr_row[col] = (
                        pick_s1 + str1[row - 1]
                        if len(pick_s1) < len(pick_s2)
                        else pick_s2 + str2[col - 1]
                    )

            prev_row = curr_row
            # print(curr_row)

        return prev_row[M]


str1 = "abac"
str2 = "cab"
# "cabac"
print(Solution().shortestCommonSupersequence(str1, str2))
