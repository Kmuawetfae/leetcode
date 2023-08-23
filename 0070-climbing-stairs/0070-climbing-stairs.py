class Solution:
    # def factorize(num):
    #     factorized_value = 1
    #     if num == 0:
    #         factorized_value = 1
    #         return factorized_value
    #     else:
    #         for i in range(num):
    #             factorized_value = factorized_value*(i + 1)
    #         return factorized_value

    def climbStairs(self, n: int) -> int:
        # i = n//2 + 1
        # j = 0

        # result = 0
        # while n > n - i + 1:
        #     # result += factorial(n)/(factorial(j)*factorial(n - j))
        #     n -= 1
        #     j += 1
        
        # return i

        if n == 1:
            return 1
        else:


            result = 2
            temp_list = [1]
            i = 1
            while i < n - 1:
                # temp_value = temp_list[i]
                temp_list.append(result)
                result += temp_list[i - 1]
                
                i += 1
            return result


        

