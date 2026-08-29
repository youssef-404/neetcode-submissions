class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) ==1:
            return len(nums)
        
        nonDep = set(nums)

        maxCon = 0
        for num in nonDep:
            if num-1 not in nonDep:
                currCon=1
                pointer = num+1
                while pointer in nonDep:
                    currCon+=1
                    pointer+=1

                maxCon = max(maxCon,currCon)
        return maxCon