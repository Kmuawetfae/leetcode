class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        for i in s:
            if ord(i.lower()) >= ord("a") and ord(i.lower()) <= ord("z") or \
            ord(i.lower()) >= ord("0") and ord(i.lower()) <= ord("9"):
                word += i.lower()
        
        if word == word[::-1]:
            return True
        else:
            return False