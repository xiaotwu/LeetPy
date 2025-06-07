# https://leetcode.com/problems/summary-ranges/description/
# [228] [Easy] Summary Ranges

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        curr_range, ranges = [], []
        start, n = 0, len(nums)
        while start < n:
            end = start
            while end + 1 < n and nums[end + 1] == nums[end] + 1:
                end += 1
            if start == end:
                curr_range = str(nums[start])
            else:
                curr_range = str(nums[start]) + "->" + str(nums[end])
            ranges.append(curr_range)
            start = end + 1
        return ranges
