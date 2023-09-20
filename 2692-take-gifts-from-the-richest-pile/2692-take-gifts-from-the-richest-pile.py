class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        while k>0:
            max_value = max(gifts)
            gifts[gifts.index(max_value)] = int(max_value ** (0.5))

            k -= 1
        
        return int(sum(gifts))