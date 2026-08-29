class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftTotal= 1
        rightTotal= 1
        length =len(nums) 
        result = [1] * length

        for i in range(length):
            result[i]= leftTotal
            leftTotal*=nums[i]

        for j in range(length-1,-1,-1):
            result[j] *= rightTotal 
            rightTotal *= nums[j]

        return result