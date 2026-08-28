class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maps = {}

        for i in nums:
            maps[i] = maps.get(i,0)+1

        res = [[] for _ in range(len(nums) + 1)]

        for idx in maps:
            value = res[maps[idx]]
            value.append(idx)

        final = []
        for j in range(len(res)):
            current = res[len(res)-j-1]
            while len(final)<k and len(current) != 0:
                final.append(current.pop())
        return final