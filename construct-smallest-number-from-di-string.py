class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = []
        num_stack = []

        for index in range(len(pattern) + 1):
            num_stack.append(index + 1)
            if index == len(pattern) or pattern[index] == "I":
                while num_stack:
                    res.append(str(num_stack.pop()))

        return "".join(res)


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        self.result = []

        self.build_sequence(0, 0, pattern)

        return "".join(self.result[::-1])

    def build_sequence(
        self, current_index: int, current_count: int, pattern: str
    ) -> int:
        if current_index != len(pattern):
            if pattern[current_index] == "I":
                self.build_sequence(current_index + 1, current_index + 1, pattern)
            else:
                current_count = self.build_sequence(
                    current_index + 1, current_count, pattern
                )

        self.result.append(str(current_count + 1))

        return current_count + 1


pattern = "IIIDIDDD"
print(Solution().smallestNumber(pattern))
