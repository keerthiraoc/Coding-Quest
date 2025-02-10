from collections import deque


class Solution:
    def clearDigits(self, s: str) -> str:
        stack = deque()
        for c in s:
            if 97 <= ord(c) <= 122:
                stack.append(c)
            else:
                stack.pop()

        return "".join(stack)


s = "cb34"

s = "abc"
print(Solution().clearDigits(s))
