
# FROM: https://leetcode.com/lc_day12/
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        d = {}
        for i, j in enumerate(nums):
            r = target - j
            print(f" current index: {i}, current num: {j}, r = {r}")
            if r in d: return [d[r], i]
            d[j] = i
            print(f"current d[j] = i: {d[j]}")


if __name__ == "__main__":
    c = Solution()
    sol = c.twoSum([5,5,11], 10)
    print(sol)
