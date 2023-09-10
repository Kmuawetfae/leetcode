class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_list = [j for j in magazine]
        for i in ransomNote:
            if i in mag_list:
                mag_list.remove(i)
            else:
                return False
        
        return True