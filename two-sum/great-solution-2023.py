
# FROM: https://leetcode.com/lc_day12/
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        d = {}
        for i, j in enumerate(nums):
            r = target - j
            if r in d: return [d[r], i]
            d[j] = i