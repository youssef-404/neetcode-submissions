class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area =0 
        left = 0
        right = len(heights) -1

        while left<right:
            width = right - left
            height = min(heights[left],heights[right])
            area = max(area,width*height)
            if heights[left]< heights[right]:
                left+=1
            else:
                right-=1
        return area