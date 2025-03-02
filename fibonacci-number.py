class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        prev, curr = 0, 1
        while n != 1:
            curr, prev = prev + curr, curr
            n -= 1

        return curr


n = 3
print(Solution().fib(n))
