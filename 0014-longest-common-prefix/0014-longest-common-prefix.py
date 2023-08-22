class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len_word_list = []

        for i in strs:
            min_len_word_list.append(len(i))
        
        min_len_word = min(min_len_word_list)

        result = 0
        for j in range(min_len_word):
            sample_word = []
            for k in strs:
                sample_word.append(k[j])
            if len(set(sample_word)) == 1:
                result += 1
            else:
                break
        
        if result == 0:
            return ""
        else:
            return strs[0][:result]