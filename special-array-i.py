from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        isSpecial = True
        for i in range(1, len(nums)):
            if nums[i - 1] % 2 == nums[i] % 2:
                isSpecial = False
                break

        return isSpecial


nums = [4, 3, 1, 6]
print(Solution().isArraySpecial(nums))
