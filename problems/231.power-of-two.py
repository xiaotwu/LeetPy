# https://leetcode.com/problems/power-of-two/description/
# [231] [Easy] Power of Two

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        max = 2 ** 30
        return n > 0 and max % n == 0
