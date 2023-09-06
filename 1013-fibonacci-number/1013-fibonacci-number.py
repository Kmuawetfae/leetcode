class Solution:
    def fib(self, n: int) -> int:
        f_n = 0
        f_n_1 = 1
        
        if n == 0:
            return 0
        elif n == 1:
            return 1

        while n > 1:
            f_n_2 = f_n_1 + f_n

            f_n = f_n_1
            f_n_1 = f_n_2

            n -=1 
        
        return f_n_2