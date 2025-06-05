# https://leetcode.com/problems/roman-to-integer/description/
# [13] [Medium] Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = [
            ('M', 1000),
            ('CM', 900),
            ('D', 500),
            ('CD', 400),
            ('C', 100),
            ('XC', 90),
            ('L', 50),
            ('XL', 40),
            ('X', 10),
            ('IX', 9),
            ('V', 5),
            ('IV', 4),
            ('I', 1),
        ]
        result = 0
        i = 0

        while i < len(s):
            for numeral, value in roman_numerals:
                if s.startswith(numeral, i):
                    result += value
                    i += len(numeral)
                    break

        return result
