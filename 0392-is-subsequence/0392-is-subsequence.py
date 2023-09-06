class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index_list = []
        j = 0
        k = 0
        for i in s:
            if i in t:
                j=t.index(i)
                k += j
                index_list.append(k)
                t = t.replace(i, " ", 1)
                t=t[j:]
            else:
                return False

        return sorted(index_list) == index_list