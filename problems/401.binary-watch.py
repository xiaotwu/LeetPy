# https://leetcode.com/problems/binary-watch/description/
# [401] [Easy] Binary Watch

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []

        def backtrack(position, hour, minute, turnedon):
            if hour > 11 or minute > 59:
                return
            if turnedon == 0:
                result.append(f"{hour}:{minute:02d}")
                return
            for i in range(position, 10):
                if i < 4:
                    backtrack(i + 1, hour + (1 << i), minute, turnedon - 1)
                else:
                    backtrack(i + 1, hour, minute + (1 << (i - 4)), turnedon - 1)

        backtrack(0, 0, 0, turnedOn)
        return result
