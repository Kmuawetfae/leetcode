class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_word1 = len(word1)
        len_word2 = len(word2)

        if len_word1 > len_word2:
            len_word = len_word2
        else:
            len_word = len_word1
        
        merged_str = ""
        for i in range(len_word):
            merged_str += word1[i]
            merged_str += word2[i]
        
        if len_word1 > len_word2:
            merged_str += word1[i+1:]
        elif len_word1 < len_word2:
            merged_str += word2[i+1:]

        return merged_str