from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[left] = nums[i]
                left += 1

        return left


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(Solution().removeDuplicates(nums))
