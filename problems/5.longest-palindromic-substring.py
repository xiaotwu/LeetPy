# https://leetcode.com/problems/longest-palindromic-substring/description/
# [5] [Medium] Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        n = len(s)
        if n < 2:
            return s
        
        dp = [[False] * n for _ in range(n)]
        start = 0
        max_length = 1

        for i in range(n):
            dp[i][i] = True

        for j in range(1, n):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i == 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j] and (j - i + 1) > max_length:
                    max_length = j - i + 1
                    start = i
            
        return s[start:start + max_length]
