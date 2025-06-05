# https://leetcode.com/problems/reverse-integer/description/
# [7] [Medium] Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_x = 0

        while x > 0:
            digit = x % 10
            x //= 10
            reversed_x = reversed_x * 10 + digit

        reversed_x *= sign
        return reversed_x if -2**31 <= reversed_x <= 2**31 - 1 else 0
    