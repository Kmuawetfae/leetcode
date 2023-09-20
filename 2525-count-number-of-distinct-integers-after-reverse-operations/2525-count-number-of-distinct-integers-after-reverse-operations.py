class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        d_dict = defaultdict(lambda:0)

        for num in nums:
            d_dict[num] = 1

        for num in nums:
            rev = int(str(num)[::-1])
            if d_dict[rev] != 1:
                d_dict[rev] = 1

        return(len(d_dict))