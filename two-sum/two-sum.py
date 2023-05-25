class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            j=i+1
            for k in range(j, len(nums)):
                if nums[i]+nums[k]==target:
                    return [i,k]

if __name__ == "__main__":
    s = Solution()
    # nums = [2,7,11,15]
    # target = 9
    # print(s.twoSum(nums, target))

    nums = [3,2,3]
    target = 6
    print(s.twoSum(nums, target))