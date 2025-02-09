class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        diff = []
        for i in range(len(s2)):
            if s1[i] != s2[i]:
                diff.append(i)

        if len(diff) != 2:
            return False

        i, j = diff
        return s1[i] == s2[j] and s2[i] == s1[j]


s1 = "bank"
s2 = "kanb"
print(Solution().areAlmostEqual(s1, s2))
