class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        chara = ""
        for i in words:
            chara += i[0]
        
        if chara == s:
            return True

        return False