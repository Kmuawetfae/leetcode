class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        check = set(banned)
        result = 0
        sum_val = 0
        for i in range(1, n + 1):
            if i not in check:
                result += 1
                sum_val += i
            
            if sum_val > maxSum:
                return(result - 1)
                
            if sum_val == maxSum:
                return(result)
        
        return result
                