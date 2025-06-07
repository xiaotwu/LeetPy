# https://leetcode.com/problems/power-of-three/description/
# [326] [Easy] Power of Three

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        max = 3 ** 19
        return n > 0 and max % n == 0
