from typing import List
import heapq


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = sorted(list(zip(nums1, nums2)), reverse=True, key=lambda ab: ab[1])
        total = res = 0
        min_heap = []
        for x, y in nums:
            heapq.heappush(min_heap, x)
            total += x

            if len(min_heap) > k:
                total -= heapq.heappop(min_heap)

            if len(min_heap) == k:
                res = max(res, total * y)

        return res


nums1 = [1, 3, 3, 2]
nums2 = [2, 1, 3, 4]
k = 3

print(Solution().maxScore(nums1, nums2, k))
