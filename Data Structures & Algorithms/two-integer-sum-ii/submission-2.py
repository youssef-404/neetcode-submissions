class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
    
        while left<right:
            sumTwo =numbers[left] +numbers[right]
            if sumTwo < target:
                left+=1
            elif sumTwo > target:
                right-=1
            else:
                return [left+1,right+1]

