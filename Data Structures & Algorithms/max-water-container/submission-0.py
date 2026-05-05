class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1

        maxVal = 0 
        while i < j: 
            temp = (j-i)*min(heights[j],heights[i])
            if temp > maxVal: 
                maxVal = temp 
            
            if heights[j] > heights[i]: 
                i += 1
            else:
                j -= 1

        return maxVal

        