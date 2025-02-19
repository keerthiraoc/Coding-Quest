class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        curr_str = ""
        happy_strings = []
        self.createHappyString(n, curr_str, happy_strings)

        if len(happy_strings) < k:
            return ""

        happy_strings.sort()
        return happy_strings[k - 1]

    def createHappyString(self, n: int, curr_str: str, happy_strings: list):
        if len(curr_str) == n:
            happy_strings.append(curr_str)
            return

        for ch in ["a", "b", "c"]:
            if curr_str == "" or curr_str[-1] != ch:
                self.createHappyString(n, curr_str + ch, happy_strings)


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.current_string = ""
        self.result = ""
        self.index_in_sorted_list = 0

        self.generate_happy_strings(n, k)
        return self.result

    def generate_happy_strings(self, n, k):
        if len(self.current_string) == n:
            self.index_in_sorted_list += 1

            if self.index_in_sorted_list == k:
                self.result = self.current_string
            return

        for current_char in ["a", "b", "c"]:
            if len(self.current_string) > 0 and self.current_string[-1] == current_char:
                continue

            self.current_string += current_char

            self.generate_happy_strings(n, k)
            if self.result != "":
                return

            self.current_string = self.current_string[:-1]


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # Calculate the total number of happy strings of length n
        total = 3 * (1 << (n - 1))

        # If k is greater than the total number of happy strings, return an empty string
        if k > total:
            return ""

        result = ["a"] * n  # Initialize result with 'a' characters

        # Define mappings for the next smallest and greatest valid characters
        next_smallest = {"a": "b", "b": "a", "c": "a"}
        next_greatest = {"a": "c", "b": "c", "c": "b"}

        # Calculate the starting indices for strings beginning with 'a', 'b', and 'c'
        start_a = 1
        start_b = start_a + (1 << (n - 1))
        start_c = start_b + (1 << (n - 1))

        # Determine the first character based on the value of k
        if k < start_b:
            result[0] = "a"
            k -= start_a
        elif k < start_c:
            result[0] = "b"
            k -= start_b
        else:
            result[0] = "c"
            k -= start_c

        # Iterate through the remaining positions in the result string
        for char_index in range(1, n):
            # Calculate the midpoint of the group for the current character position
            midpoint = 1 << (n - char_index - 1)

            # Determine the next character based on the value of k
            if k < midpoint:
                result[char_index] = next_smallest[result[char_index - 1]]
            else:
                result[char_index] = next_greatest[result[char_index - 1]]
                k -= midpoint

        return "".join(result)


n = 1
k = 3
n = 3
k = 9
print(Solution().getHappyString(n, k))
