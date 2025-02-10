from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        N = len(costs)
        first_candidates, last_candidates = (
            costs[:candidates],
            costs[max(candidates, N - candidates) :],
        )
        heapify(first_candidates)
        heapify(last_candidates)

        total_cost = 0
        first_pointer, last_pointer = candidates, len(costs) - 1 - candidates
        for _ in range(k):
            if (
                not last_candidates
                or first_candidates
                and first_candidates[0] <= last_candidates[0]
            ):
                total_cost += heappop(first_candidates)
                if first_pointer <= last_pointer:
                    heappush(first_candidates, costs[first_pointer])
                    first_pointer += 1
            else:
                total_cost += heappop(last_candidates)
                if first_pointer <= last_pointer:
                    heappush(last_candidates, costs[last_pointer])
                    last_pointer -= 1

        return total_cost


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        pq = []
        for i in range(candidates):
            pq.append((costs[i], 0))
        for i in range(max(candidates, len(costs) - candidates), len(costs)):
            pq.append((costs[i], 1))

        heapify(pq)

        answer = 0
        next_head, next_tail = candidates, len(costs) - 1 - candidates

        for _ in range(k):
            cur_cost, cur_section_id = heappop(pq)
            answer += cur_cost
            if next_head <= next_tail:
                if cur_section_id == 0:
                    heappush(pq, (costs[next_head], 0))
                    next_head += 1
                else:
                    heappush(pq, (costs[next_tail], 1))
                    next_tail -= 1

        return answer


costs = [17, 12, 10, 2, 7, 2, 11, 20, 8]
k = 3
candidates = 4

print(Solution().totalCost(costs, k, candidates))
