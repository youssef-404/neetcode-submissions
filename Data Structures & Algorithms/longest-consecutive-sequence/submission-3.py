class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) ==1:
            return len(nums)
        
        nums = sorted(nums)

        maxCon = 1
        current = 1 
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1] - 1:
                current +=1
                continue
            elif nums[i] == nums[i+1]:
                continue
            
            if maxCon<current:
                maxCon = current
            current =1

        if maxCon<current:
            maxCon = current
        return maxCon