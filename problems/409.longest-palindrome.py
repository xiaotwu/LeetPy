# https://leetcode.com/problems/longest-palindrome/description/
# [409] [Easy] Longest Palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        length = 0
        odd_found = False
        for freq in count.values():
            if freq % 2 == 0:
                length += freq
            else:
                length += freq - 1
                odd_found = True
        return length + (1 if odd_found else 0)
