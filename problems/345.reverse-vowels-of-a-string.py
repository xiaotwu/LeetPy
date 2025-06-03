# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
# [345] [Easy] Reverse Vowels of a String

class Solution:
    def reverseVowels(self, s: str) -> str:
        mapping = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] not in mapping:
                left += 1
            elif s[right] not in mapping:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return ''.join(s)
