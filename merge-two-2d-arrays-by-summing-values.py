from typing import List


class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        ptr1 = ptr2 = 0
        N1, N2 = len(nums1), len(nums2)

        res = []
        while ptr1 < N1 and ptr2 < N2:
            if nums1[ptr1][0] == nums2[ptr2][0]:
                res.append([nums1[ptr1][0], nums1[ptr1][1] + nums2[ptr2][1]])
                ptr1 += 1
                ptr2 += 1

            elif nums1[ptr1][0] > nums2[ptr2][0]:
                res.append(nums2[ptr2])
                ptr2 += 1

            elif nums1[ptr1][0] < nums2[ptr2][0]:
                res.append(nums1[ptr1])
                ptr1 += 1

        while ptr1 < N1:
            res.append(nums1[ptr1])
            ptr1 += 1

        while ptr2 < N2:
            res.append(nums2[ptr2])
            ptr2 += 1

        return res


nums1 = [[1, 2], [2, 3], [4, 5]]
nums2 = [[1, 4], [3, 2], [4, 1]]
# nums1 = []
# nums2 = []

print(Solution().mergeArrays(nums1, nums2))
