class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxLeft = height[left]
        maxRight = height[right]
        res = 0
        while left < right :
            if maxLeft<= maxRight:
                res+= (maxLeft - height[left])
                left+=1
                maxLeft= max(maxLeft,height[left])
            else:
                res+= (maxRight - height[right])
                right-=1
                maxRight= max(maxRight,height[right])

        return res 