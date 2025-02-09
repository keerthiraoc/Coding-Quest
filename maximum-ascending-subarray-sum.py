from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = 0
        currSubarraySum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                maxSum = max(maxSum, currSubarraySum)
                currSubarraySum = 0

            currSubarraySum += nums[i]

        return max(maxSum, currSubarraySum)


nums = [10, 20, 30, 5, 10, 50]
print(Solution().maxAscendingSum(nums))
