class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res =set()
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left < right:
                calc = nums[left]+ nums[right]+nums[i]
                if calc < 0:
                    left+=1
                elif calc > 0:
                    right-=1
                else:
                    res.add((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1
        return list(list(sol) for sol in res) 