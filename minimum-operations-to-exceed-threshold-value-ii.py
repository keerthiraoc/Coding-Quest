from typing import List
import heapq


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        count = 0
        while len(nums) > 1 and nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))
            count += 1
        return count


nums = [2, 11, 10, 1, 3]
k = 10
print(Solution().minOperations(nums, k))
