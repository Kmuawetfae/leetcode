class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        i = 1
        sum_val = 0
        result = 0
        check = set(banned)
        while sum_val <= maxSum and i <= n:
            if i not in check:
                sum_val += i
                result += 1
            i += 1

        return result if sum_val < maxSum else result - 1
                