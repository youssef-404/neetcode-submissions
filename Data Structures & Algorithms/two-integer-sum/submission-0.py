class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counts = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in counts:
                return [min(i,counts[diff]),max(i,counts[diff])]
            counts[nums[i]] = i