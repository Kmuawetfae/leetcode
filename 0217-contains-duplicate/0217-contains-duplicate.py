class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_list = set(nums)
        return len(set_list) != len(nums)