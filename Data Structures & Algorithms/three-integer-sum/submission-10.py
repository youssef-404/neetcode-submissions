class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        solution = []
        for current in range(len(nums)-2):
            left = current+1
            right =len(nums)-1
            if nums[current]>0:
                break
            if current>0 and nums[current] == nums[current-1]:
                continue
            
            while left<right:
                calc = nums[left]+nums[right]+nums[current]
                if calc == 0:
                    solution.append((nums[current],nums[left],nums[right]))
                    left+=1
                    right-=1
                    while left < right and nums[left] ==  nums[left-1]:
                        left+=1
                    while left < right and nums[right] ==  nums[right+1]:
                        right-=1
                elif calc <0:
                    left+=1
                else:
                    right-=1
        return solution
        
    
