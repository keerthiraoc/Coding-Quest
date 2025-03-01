from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        N = len(nums)
        for i in range(N - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0

        left = 0
        for right in range(N):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1

        return nums


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        N = len(nums)
        write_index = 0

        for i in range(N):
            if i < N - 1 and nums[i] == nums[i + 1] and nums[i] != 0:
                nums[i] *= 2
                nums[i + 1] = 0

            if nums[i] != 0:
                nums[i], nums[write_index] = nums[write_index], nums[i]
                write_index += 1

        return nums


nums = [1, 2, 2, 1, 1, 0]
print(Solution().applyOperations(nums))
