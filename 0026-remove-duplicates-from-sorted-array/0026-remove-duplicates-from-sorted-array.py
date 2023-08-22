class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        set_nums = set(nums)

        for i in set_nums:
            while i in nums:
                nums.remove(i)
        
        for j in set_nums:
            nums.append(j)
        
        nums.sort()
        return len(nums)
