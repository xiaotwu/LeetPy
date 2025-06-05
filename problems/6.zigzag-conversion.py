# https://leetcode.com/problems/zigzag-conversion/description/
# [6] [Medium] Zigzag Conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [''] * numRows
        current_row = 0
        down = False

        for char in s:
            rows[current_row] += char
            if current_row == 0:
                down = True
            if current_row == numRows - 1:
                down = False
            current_row += 1 if down else -1

        return ''.join(rows)
