class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length_input = len(s)
        factorize_input = []

        for i in range(1, int(length_input/2) + 1):
            if length_input%i == 0:
                factorize_input.append(i)
        
        for j in factorize_input:
            sub_string_list = []
            k = 0
            while k < length_input:
                sub_string_list.append(s[k:k+j])
                k += j
            sub_string_list = set(sub_string_list)
            if len(sub_string_list) == 1:
                return True
        
        return False