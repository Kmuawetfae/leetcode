class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            str_int = str(x*(-1))
        else:
            str_int = str(x)
        str_int_reversed = str_int[::-1]

        if x < 0:
            str_int_reversed = int(str_int_reversed) * (-1)
        else:
            str_int_reversed = int(str_int_reversed)
        
        if str_int_reversed < 2**31 - 1 and str_int_reversed > (-2)**31:
            return str_int_reversed
        else:
            return 0
            
