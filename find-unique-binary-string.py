from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        self.nums_set = set(nums)

        return self.generateBinaryString("", len(nums))

    def generateBinaryString(self, curr_string, n):
        if len(curr_string) == n:
            if curr_string not in self.nums_set:
                return curr_string
            return ""

        return self.generateBinaryString(
            curr_string + "0", n
        ) or self.generateBinaryString(curr_string + "1", n)


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        integers = set()
        for num in nums:
            integers.add(int(num, 2))

        n = len(nums)
        for num in range(n + 1):
            if num not in integers:
                ans = bin(num)[2:]
                return "0" * (n - len(ans)) + ans

        return ""


# Based on Cantor's Diagonal Argument (Don't try this)
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = []
        for i in range(len(nums)):
            curr = nums[i][i]
            ans.append("1" if curr == "0" else "0")

        return "".join(ans)


nums = ["01", "10"]
print(Solution().findDifferentBinaryString(nums))
