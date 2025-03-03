from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lesser, greater = [], []
        count = 0
        for num in nums:
            if num < pivot:
                lesser.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                count += 1
        nums = lesser + [pivot] * count + greater
        return nums


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lesser_num_idx, equal_num_idx = 0, 0
        for num in nums:
            if num < pivot:
                lesser_num_idx += 1
            elif num == pivot:
                equal_num_idx += 1

        res = [0] * len(nums)
        i, j = 0, lesser_num_idx + equal_num_idx
        for num in nums:
            if num < pivot:
                res[i] = num
                i += 1
            elif num > pivot:
                res[j] = num
                j += 1
            else:
                res[lesser_num_idx] = num
                lesser_num_idx += 1

        return res


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        N = len(nums)
        ans = [0] * N
        less_idx, greater_idx = 0, N - 1
        for i, j in zip(range(N), range(N - 1, -1, -1)):
            if nums[j] > pivot:
                ans[greater_idx] = nums[j]
                greater_idx -= 1

            if nums[i] < pivot:
                ans[less_idx] = nums[i]
                less_idx += 1

        while less_idx <= greater_idx:
            ans[less_idx] = pivot
            less_idx += 1

        return ans


nums = [9, 12, 5, 10, 14, 3, 10]
pivot = 10
print(Solution().pivotArray(nums, pivot))
