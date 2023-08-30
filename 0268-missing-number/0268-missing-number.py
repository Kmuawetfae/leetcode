class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if 0 not in nums:
            return 0
        nums.sort()
        for i in range(len(nums)):
            if i + 1 == len(nums):
                return i + 1
            elif i + 1 != nums[i + 1]:
                return i + 1