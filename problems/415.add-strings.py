# https://leetcode.com/problems/add-strings/description/
# [415] [Easy] Add Strings

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        add = 0
        result = []
        i, j = len(num1) - 1, len(num2) - 1
        while i >= 0 or j >= 0 or add:
            if i >= 0:
                add += ord(num1[i]) - ord('0')
                i -= 1

            if j >= 0:
                add += ord(num2[j]) - ord('0')
                j -= 1

            result.append(chr(add % 10 + ord('0')))
            add //= 10

        return ''.join(reversed(result))
