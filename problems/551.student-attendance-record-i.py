# https://leetcode.com/problems/student-attendance-record-i/description/
# [551] [Easy] Student Attendance Record I

class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count('A') < 2 and 'LLL' not in s
