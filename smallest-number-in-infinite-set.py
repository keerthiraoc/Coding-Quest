import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.curr = 1
        self.min_heap = []
        self.nums = set()

    def popSmallest(self) -> int:
        if not self.min_heap:
            smallest = self.curr
            self.curr += 1
        else:
            smallest = heapq.heappop(self.min_heap)
            self.nums.remove(smallest)
        return smallest

    def addBack(self, num: int) -> None:
        if num < self.curr and num not in self.nums:
            heapq.heappush(self.min_heap, num)
            self.nums.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
