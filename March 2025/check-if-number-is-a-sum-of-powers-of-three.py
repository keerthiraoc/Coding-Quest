class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        return self._check_powers_of_three_helper(0, n)

    def _check_powers_of_three_helper(self, power: int, n: int) -> bool:
        if n == 0:
            return True

        if 3**power > n:
            return False

        add_power = self._check_powers_of_three_helper(power + 1, n - 3**power)
        skip_power = self._check_powers_of_three_helper(power + 1, n)

        return add_power or skip_power


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        power = 0

        while 3**power <= n:
            power += 1

        while n > 0:
            if n >= 3**power:
                n -= 3**power
            if n >= 3**power:
                return False
            power -= 1

        return True


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True


n = 12
# n = 91
# n = 21
print(Solution().checkPowersOfThree(n))
