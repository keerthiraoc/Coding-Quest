from collections import defaultdict
from sortedcontainers import SortedSet
import heapq


class NumberContainers:
    def __init__(self):
        self.index_to_number = {}
        self.number_to_indices = defaultdict(SortedSet)

    def change(self, index: int, number: int) -> None:
        if index in self.index_to_number:
            previous_number = self.index_to_number[index]
            self.number_to_indices[previous_number].remove(index)

            if not self.number_to_indices[previous_number]:
                del self.number_to_indices[previous_number]

        self.index_to_number[index] = number
        self.number_to_indices[number].add(index)

    def find(self, number: int) -> int:
        if number in self.number_to_indices and self.number_to_indices[number]:
            return self.number_to_indices[number][0]

        return -1


class NumberContainers:
    def __init__(self):
        self.number_to_indices = defaultdict(list)
        self.index_to_numbers = {}

    def change(self, index: int, number: int) -> None:
        self.index_to_numbers[index] = number
        heapq.heappush(self.number_to_indices[number], index)

    def find(self, number: int) -> int:
        if not self.number_to_indices[number]:
            return -1

        while self.number_to_indices[number]:
            index = self.number_to_indices[number][0]

            if self.index_to_numbers.get(index) == number:
                return index

            heapq.heappop(self.number_to_indices[number])

        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)

actions = [
    "find",
    "change",
    "change",
    "change",
    "change",
    "find",
    "change",
    "find",
]
params = [[10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]

obj = NumberContainers()
for i in range(len(actions)):
    action = actions[i]
    param = params[i]

    # Dynamically call the method based on the action
    if action == "change":
        obj.change(*param)
    elif action == "find":
        result = obj.find(*param)
        print(result)
