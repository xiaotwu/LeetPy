# https://leetcode.com/problems/integer-to-roman/description/
# [12] [Medium] Integer to Roman

class Solution:
    def intToRoman(self, num: int) -> str:
        roman_numerals = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        result = []

        for value, numeral in roman_numerals:
            while num >= value:
                result.append(numeral)
                num -= value
        
        return ''.join(result)
