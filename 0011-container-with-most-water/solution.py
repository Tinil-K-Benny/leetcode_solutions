class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        l, r = 0, len(height) - 1
        max_water = 0

        while l < r:
            width = r -l
            current_water = min(height[r],height[l])*width
            max_water = max(current_water,max_water)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_water


