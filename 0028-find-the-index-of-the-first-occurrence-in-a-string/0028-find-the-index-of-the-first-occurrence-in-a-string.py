class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            length_n = len(needle)
            i = 0
            while i < len(haystack):
                if haystack[i:i+length_n] == needle:
                    return i
                i += 1