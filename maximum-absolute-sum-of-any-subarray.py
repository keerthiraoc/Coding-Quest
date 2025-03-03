from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_prefix_sum = float("inf")
        max_prefix_sum = float("-inf")

        max_abs_sum, prefix_sum = 0, 0
        for num in nums:
            prefix_sum += num

            min_prefix_sum = min(prefix_sum, min_prefix_sum)
            max_prefix_sum = max(prefix_sum, max_prefix_sum)

            if prefix_sum >= 0:
                max_abs_sum = max(
                    max_abs_sum, max(prefix_sum, prefix_sum - min_prefix_sum)
                )
            elif prefix_sum <= 0:
                max_abs_sum = max(
                    max_abs_sum, max(abs(prefix_sum), abs(prefix_sum - max_prefix_sum))
                )

        return max_abs_sum


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_prefix_sum = 0
        max_prefix_sum = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num

            min_prefix_sum = min(prefix_sum, min_prefix_sum)
            max_prefix_sum = max(prefix_sum, max_prefix_sum)

        return max_prefix_sum - min_prefix_sum


# nums = [1, -3, 2, 3, -4]
# nums = [2, -5, 1, -4, 3, -2]
nums = [-7, -1, 0, -2, 1, 3, 8, -2, -6, -1, -10, -6, -6, 8, -4, -9, -4, 1, 4, -9]
nums = [-3, -5, -3, -2, -6, -10, -8, -3, 0]


print(Solution().maxAbsoluteSum(nums))
