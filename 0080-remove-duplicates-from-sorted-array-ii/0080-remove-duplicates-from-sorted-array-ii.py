class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Length of the array
        n = len(nums)

        # Early exit if the array has fewer than 3 elements
        if n <= 2:
            return n

        # Pointer for the position of the next valid element
        write_index = 2

        # Start iterating from the 2nd index
        for i in range(2, n):
            # Check if the current number is different from the number two places behind
            if nums[i] != nums[write_index - 2]:
                nums[write_index] = nums[i]
                write_index += 1

        return write_index