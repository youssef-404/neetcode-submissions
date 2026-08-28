class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        unique = {}

        if len(s) != len(t): return False
        for i in range(len(s)):
            unique[s[i]] = unique.get(s[i], 0) + 1
            unique[t[i]] = unique.get(t[i], 0) - 1

        for i in unique.values():
            if i != 0 :
                return False


        return True