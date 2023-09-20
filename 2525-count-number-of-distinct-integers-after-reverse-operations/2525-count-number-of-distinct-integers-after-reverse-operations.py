class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        new_nums = []
        for i in nums:
            new_nums.append(int(str(i)[::-1]))
        nums += (new_nums)

        return len(set(nums))