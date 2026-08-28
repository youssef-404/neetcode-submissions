class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashed = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in hashed:
                hashed[sorted_s] = []
            hashed[sorted_s].append(s)

        res = []
        for i in hashed:
            res.append(list(hashed[i]))
        return res