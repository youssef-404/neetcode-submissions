class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashed = {}
        for s in strs:
            set_s = sorted(s)
            sorted_s =""
            for i in set_s:
                sorted_s+=i
            if sorted_s not in hashed:
                hashed[sorted_s] = []
            hashed[sorted_s].append(s)

        res = []
        for i in hashed:
            res.append(list(hashed[i]))
        return res