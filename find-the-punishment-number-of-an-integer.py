class Solution:
    def backtrack(self, string_num, target):
        if not string_num and target == 0:
            return True

        if target < 0:
            return False

        for index in range(len(string_num)):
            left = string_num[: index + 1]
            right = string_num[index + 1 :]
            left_num = int(left)

            if self.backtrack(right, target - left_num):
                return True

        return False

    def punishmentNumber(self, n: int) -> int:
        punishment_num = 0
        for curr_num in range(1, n + 1):
            square_num = curr_num * curr_num

            if self.backtrack(str(square_num), curr_num):
                punishment_num += square_num

        return punishment_num


class Solution:
    def backtrack(self, num, target):
        if target < 0 or num < target:
            return False

        if num == target:
            return True

        return (
            self.backtrack(num // 10, target - num % 10)
            or self.backtrack(num // 100, target - num % 100)
            or self.backtrack(num // 1000, target - num % 1000)
        )

    def punishmentNumber(self, n: int) -> int:
        punishment_num = 0
        for curr_num in range(1, n + 1):
            square_num = curr_num * curr_num

            if self.backtrack(square_num, curr_num):
                punishment_num += square_num

        return punishment_num


n = 10
print(Solution().punishmentNumber(n))
