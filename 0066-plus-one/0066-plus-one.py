class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[len(digits)-1] += 1
        i = len(digits)
        while i>=0:
            if len(str(digits[i-1])) == 2:
                digits[i-1] = 0
                if i-1==0:
                    digits.insert(0, 1)
                else:
                    digits[i-2] += 1
            i-=1
            
        return digits