class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        maps = set()
        for num in nums:
            if num in maps:
                return True
            maps.add(num)
        return False