# https://leetcode.com/problems/find-the-difference/description/
# [389] [Easy] Find the Difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for char in s + t:
            res ^= ord(char)
        return chr(res)
