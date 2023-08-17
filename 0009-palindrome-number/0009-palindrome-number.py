class Solution:
    def isPalindrome(self, x: int) -> bool:
        palindrom_word = str(x)

        len_palindrom = len(palindrom_word)
        #take the half of the length of the palindrom word and round it down to the nearest int
        half_ln_palin = int(len(palindrom_word)/2)

        if palindrom_word[:half_ln_palin] == palindrom_word[-1:-half_ln_palin-1:-1]:
            return True
        else:
            return False