class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        track = set()
        for num in nums:
            if num in track:
                return True
            track.add(num)
        return False