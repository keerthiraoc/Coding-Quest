from typing import List
from collections import defaultdict


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        N = len(nums)
        pair_products = defaultdict(int)
        total_number_of_tuples = 0

        for i in range(N):
            for j in range(i + 1, N):
                pair_products[nums[i] * nums[j]] += 1

        for freq in pair_products.values():
            pairs = (freq - 1) * freq // 2
            total_number_of_tuples += 8 * pairs

        return total_number_of_tuples


nums = [1, 2, 4, 5, 10]
print(Solution().tupleSameProduct(nums))
