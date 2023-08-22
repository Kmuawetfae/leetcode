class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # set_nums = set(nums)

        # for i in set_nums:
        #     while i in nums:
        #         nums.remove(i)
        
        # for j in set_nums:
        #     nums.append(j)
        
        # nums.sort()
        # return len(nums)
        set_nums = list(set(nums))

        index_list = []
        for i in set_nums:
            index = 0
            for j in nums:
                if i == j:
                    index += 1
            index_list.append(index)
        
        for i in range(len(set_nums)):
            for j in range(index_list[i] - 1):
                nums.remove(set_nums[i])
        
        return len(nums)
            