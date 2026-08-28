class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = set()
        for i in nums:
            if i in counts:
                return True
            counts.add(i)
        return False