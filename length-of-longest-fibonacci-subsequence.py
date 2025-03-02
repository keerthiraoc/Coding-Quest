from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        arr_map = {num: idx for idx, num in enumerate(arr)}

        count = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                temp = arr[i] + arr[j]
                if temp in arr_map:
                    fib = [arr[i], arr[j], temp]
                    while fib[-1] <= arr[-1]:
                        if fib[-2] + fib[-1] in arr_map:
                            fib.append(fib[-2] + fib[-1])
                        else:
                            break
                    count = max(count, len(fib))

        return count


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        arr_set = set(arr)
        N = len(arr)

        max_count = 0
        for i in range(N):
            for j in range(i + 1, N):
                prev, curr = arr[j], arr[i] + arr[j]
                count = 2
                while curr in arr_set:
                    prev, curr = curr, prev + curr
                    count += 1
                    max_count = max(max_count, count)

        return max_count


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        N = len(arr)
        max_len = 0
        dp = [[0] * N for _ in range(N)]

        val_to_idx = {num: idx for idx, num in enumerate(arr)}

        for curr in range(N):
            for prev in range(curr):
                diff = arr[curr] - arr[prev]
                prev_idx = val_to_idx.get(diff, -1)

                dp[prev][curr] = (
                    dp[prev_idx][prev] + 1 if diff < arr[prev] and prev_idx >= 0 else 2
                )

                max_len = max(max_len, dp[prev][curr])

        return max_len if max_len > 2 else 0


# understood only two sum part
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        max_len = 0

        for curr in range(2, n):
            start = 0
            end = curr - 1

            while start < end:
                print(start, end, dp)
                pair_sum = arr[start] + arr[end]

                if pair_sum > arr[curr]:
                    end -= 1
                elif pair_sum < arr[curr]:
                    start += 1
                else:
                    dp[end][curr] = dp[start][end] + 1
                    max_len = max(max_len, dp[end][curr])
                    end -= 1
                    start += 1

        return max_len + 2 if max_len else 0


arr = [1, 2, 3, 4, 5, 6, 7, 8]
# arr = [1, 3, 7, 11, 12, 14, 18]
print(Solution().lenLongestFibSubseq(arr))
