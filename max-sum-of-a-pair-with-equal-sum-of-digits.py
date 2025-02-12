from typing import List
from collections import defaultdict


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sum_digits = defaultdict(int)
        max_sum = -1
        for num in nums:
            digit_sum = 0
            temp_num = num
            while temp_num:
                temp_num, curr_digit = divmod(temp_num, 10)
                digit_sum += curr_digit

            if digit_sum in sum_digits:
                max_sum = max(max_sum, sum_digits[digit_sum] + num)

            sum_digits[digit_sum] = max(sum_digits[digit_sum], num)

        return max_sum


# nums = [18, 43, 36, 13, 7]
nums = [
    229,
    398,
    269,
    317,
    420,
    464,
    491,
    218,
    439,
    153,
    482,
    169,
    411,
    93,
    147,
    50,
    347,
    210,
    251,
    366,
    401,
]
print(Solution().maximumSum(nums))
