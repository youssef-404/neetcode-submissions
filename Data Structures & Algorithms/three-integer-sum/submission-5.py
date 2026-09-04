class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        left = 1
        right =len(nums)-1
        solution = set()
        for current in range(len(nums)-2):
            left = current+1
            right =len(nums)-1
            while left<right:
                if nums[left]+nums[right]== -nums[current]:
                    solution.add((nums[current],nums[left],nums[right]))
                    left+=1
                    right-=1
                elif nums[left]+nums[right] < -nums[current]:
                    left+=1
                else:
                    right-=1
        return list(list(sol) for sol in solution)
        
    
