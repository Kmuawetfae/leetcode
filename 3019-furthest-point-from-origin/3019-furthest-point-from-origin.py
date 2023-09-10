class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        r_chara = moves.count("R")
        l_chara = moves.count("L")
        if r_chara >= l_chara:
            return r_chara + moves.count("_") - l_chara
        return l_chara + moves.count("_") - r_chara