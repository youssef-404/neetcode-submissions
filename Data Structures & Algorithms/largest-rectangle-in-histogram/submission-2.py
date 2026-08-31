class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack =[]
        area = 0
        heights.append(-1)
        for i in range(len(heights)):
            while stack and heights[i]<heights[stack[-1]]:
                idx = stack.pop()
                left = -1
                if stack:
                    left= stack[-1]
                area = max((i-left-1)*heights[idx],area)
          
            stack.append(i)
        return area