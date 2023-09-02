class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            for j in matrix:
                if target in j:
                    return True
        
        return False