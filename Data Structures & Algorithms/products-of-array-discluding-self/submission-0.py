class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        n = len(nums)
        left = [1] * n
        right = [1] * n
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
            right[n-i-1] = right[n-i] * nums[n-i]

        result = []
        for i in range(n):
            result.append(left[i]*right[i])
        return result