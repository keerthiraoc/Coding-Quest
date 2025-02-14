class ProductOfNumbers:

    def __init__(self):
        self.nums = []

    def add(self, num: int) -> None:
        if num == 0:
            self.nums = []
            return None

        if not self.nums:
            self.nums.append(num)
        else:
            product = self.nums[-1]
            self.nums.append(product * num)

    def getProduct(self, k: int) -> int:
        if k == len(self.nums):
            return self.nums[-1]

        if k > len(self.nums):
            return 0

        return self.nums[-1] // self.nums[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
