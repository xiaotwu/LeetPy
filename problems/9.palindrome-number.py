# https://leetcode.com/problems/palindrome-number/description/
# [9] [Easy] Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reversed_x = 0
        original_x = x

        while x > 0:
            digit = x % 10
            reversed_x = reversed_x * 10 + digit
            x //= 10

        return original_x == reversed_x
