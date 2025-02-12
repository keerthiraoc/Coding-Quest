class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = ""
        N = len(part)
        for i in range(len(s)):
            stack += s[i]
            if stack[-N:] == part:
                stack = stack[:-N]
        return stack


s = "daabcbaabcbc"
part = "abc"

print(Solution().removeOccurrences(s, part))
