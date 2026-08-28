class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nonDup = set(nums)

        res = 0
        for i in nonDup:
            if i-1 not in nonDup:
                size=1
                j=i+1
                while j in nonDup:
                    size+=1
                    j+=1
                if res<size:
                    res=size
        return res