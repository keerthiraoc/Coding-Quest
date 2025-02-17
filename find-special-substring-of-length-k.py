class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        curr_count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr_count += 1
            else:
                if curr_count == k:
                    return True
                curr_count = 1
        return curr_count == k
