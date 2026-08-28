class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for idx in range(len(nums)):
            rest = target - nums[idx]
            if rest in maps:
                return [maps.get(rest),idx]
            maps[nums[idx]] = idx