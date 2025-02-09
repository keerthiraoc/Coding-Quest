import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        largest = []
        for num in nums:
            heapq.heappush(largest, num)
            while len(largest) > k:
                heapq.heappop(largest)

        return heapq.heappop(largest)


# try solving using quick sort and divide conquer methods


nums = [3, 2, 1, 5, 6, 4]
k = 2

print(Solution().findKthLargest(nums, k))
