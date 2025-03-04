from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        odd_sum = even_sum = 0
        total = ans = 0
        for num in arr:
            total += num
            if total % 2 == 0:
                even_sum += 1
                ans += odd_sum
            else:
                odd_sum += 1
                ans += even_sum + 1

        return ans % MOD


arr = [1, 3, 5]
print(Solution().numOfSubarrays(arr))
