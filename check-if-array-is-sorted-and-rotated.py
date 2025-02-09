from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        N = len(nums)
        if N <= 1:
            return True

        rotated = 0
        for i in range(1, N):
            if nums[i] < nums[i - 1]:
                rotated += 1

        if nums[0] < nums[-1]:
            rotated += 1

        return rotated <= 1


nums = [3, 4, 5, 1, 2]
nums = [2, 1, 3, 4]
print(Solution().check(nums))
