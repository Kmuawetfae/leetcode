class Solution:
    def pivotInteger(self, n: int) -> int:
        sum_all = int(sum([i for i in range(1, n + 1)]))
        value = 0
        for i in range(1, n + 1):
            value += i
            if value == (sum_all - value + i):
                return(i)
        return(-1)