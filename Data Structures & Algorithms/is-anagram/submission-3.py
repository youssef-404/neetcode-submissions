class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        indexS = {}
        indexT = {}
        for i in range(len(s)):
            indexS[s[i]] = indexS.get(s[i], 0) + 1
            indexT[t[i]] = indexT.get(t[i], 0) + 1
        
        return indexT == indexS