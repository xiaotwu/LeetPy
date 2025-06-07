# https://leetcode.com/problems/powx-n/description/
# [50] [Medium] Pow(x, n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0:
            return 0.0
        if n < 0:
            x, n = 1 / x, -n
        result = 1.0
        while n:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2

        return result
