class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        
        total_number = 0
        i = 0
        
        while i < len(s):
            cur_char = s[i]
            if i + 1 == len(s):
                nxt_char = s[i]
            else:
                nxt_char = s[i + 1]
            if roman_dict[cur_char] < roman_dict[nxt_char]:
                total_number += roman_dict[nxt_char] - roman_dict[cur_char]
                i += 2
            else:
                total_number += roman_dict[cur_char]
                i += 1

        return total_number
