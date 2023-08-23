class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_set = set(nums)
        nums_unique = list(nums_set)

        nums_of_num_list = []
        for i in nums_unique:
            nums_of_num = 0
            for j in nums:
                if i == j:
                    nums_of_num += 1
            nums_of_num_list.append(nums_of_num)
        
        max_index = nums_of_num_list.index(max(nums_of_num_list))

        return nums_unique[max_index]

