# https://leetcode.com/problems/robot-return-to-origin/description/
# [657] [Easy] Robot Return to Origin

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dx = {'U': 0, 'D': 0, 'L': -1, 'R': 1}
        dy = {'U': 1, 'D': -1, 'L': 0, 'R': 0}
        x, y = 0, 0

        for move in moves:
            x += dx[move]
            y += dy[move]
        
        return x == 0 and y == 0
