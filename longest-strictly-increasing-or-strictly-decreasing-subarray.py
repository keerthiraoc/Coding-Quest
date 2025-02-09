from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_length = inc_length = dec_length = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                inc_length += 1
                dec_length = 1
            elif nums[i + 1] < nums[i]:
                dec_length += 1
                inc_length = 1
            else:
                dec_length = inc_length = 1

            max_length = max(max_length, inc_length, dec_length)

        return max_length


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_length = 1
        N = len(nums)

        temp_length = 1
        for i in range(1, N):
            if nums[i] > nums[i - 1]:
                temp_length += 1
                max_length = max(temp_length, max_length)
            else:
                temp_length = 1

        temp_length = 1
        for i in range(1, N):
            if nums[i] < nums[i - 1]:
                temp_length += 1
                max_length = max(temp_length, max_length)
            else:
                temp_length = 1

        return max_length


nums = [1, 4, 3, 3, 2]
nums = [21, 32, 1, 39, 40, 24, 6, 21, 24, 33, 25, 33, 6, 50, 34, 14, 24, 12, 2, 1]
print(Solution().longestMonotonicSubarray(nums))
