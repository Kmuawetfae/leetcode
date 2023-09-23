class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence_list = sentence.split(" ")
        last_word = sentence_list[0][len(sentence_list[0]) - 1]

        for i in sentence_list[1:]:
            first_word = i[0]
            if (first_word != last_word):
                return False
            last_word = i[len(i) - 1]

        if last_word != sentence_list[0][0]:
            return False
        
        return True