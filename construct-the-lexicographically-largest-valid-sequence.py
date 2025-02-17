from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res_sequence = [0] * (n * 2 - 1)
        is_number_used = [False] * (n + 1)

        self.find_lexicographically_largest_sequence(0, res_sequence, is_number_used, n)

        return res_sequence

    def find_lexicographically_largest_sequence(
        self, curr_idx, res_sequence, is_number_used, n
    ):
        if curr_idx == len(res_sequence):
            return True

        if res_sequence[curr_idx] != 0:
            return self.find_lexicographically_largest_sequence(
                curr_idx + 1, res_sequence, is_number_used, n
            )

        for num in range(n, 0, -1):
            if is_number_used[num]:
                continue

            is_number_used[num] = True
            res_sequence[curr_idx] = num

            if num == 1:
                if self.find_lexicographically_largest_sequence(
                    curr_idx + 1, res_sequence, is_number_used, n
                ):
                    return True
            elif (
                curr_idx + num < len(res_sequence) and res_sequence[curr_idx + num] == 0
            ):
                res_sequence[curr_idx + num] = num

                if self.find_lexicographically_largest_sequence(
                    curr_idx + 1, res_sequence, is_number_used, n
                ):
                    return True

                res_sequence[curr_idx + num] = 0

            res_sequence[curr_idx] = 0
            is_number_used[num] = False

        return False


n = 5

print(Solution().constructDistancedSequence(n))
