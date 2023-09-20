class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        total, i, j = 0, 0, len(nums)-1

        while i < j:
            if nums[i] + nums[j] > upper:
                j -= 1
            else:
                total += j-i
                i += 1

        i, j = 0, len(nums)-1

        while i < j:
            if nums[i] + nums[j] > lower-1:
                j -= 1
            else:
                total -= j-i
                i += 1

        return total