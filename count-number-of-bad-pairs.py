from typing import List
from collections import defaultdict


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        pairs_diff = defaultdict(int)
        bad_pairs = 0
        for i in range(len(nums)):
            diff = nums[i] - i
            bad_pairs += i - pairs_diff[diff]
            pairs_diff[diff] += 1
        return bad_pairs


nums = [4, 1, 3, 3]
# nums = [1, 2, 3, 4, 5]

print(Solution().countBadPairs(nums))
