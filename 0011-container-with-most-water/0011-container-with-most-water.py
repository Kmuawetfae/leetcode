class Solution:
    def maxArea(self, height: List[int]) -> int:
        ind_1 = 0
        ind_2 = len(height) - 1
        max_area = 0
        
        while ind_1 < ind_2:
            area = (ind_2 - ind_1) * min(height[ind_1], height[ind_2])
            
            max_area = max(max_area, area)
            
            if height[ind_1] < height[ind_2]:
                ind_1 += 1
            else:
                ind_2 -= 1
        
        return max_area