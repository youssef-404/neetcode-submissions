class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        mapS = {}
        for alpha in s:
            if alpha in mapS:
                mapS[alpha]+=1
            else:
                mapS[alpha]=1
        for alpha in t:
            if alpha in mapS:
                mapS[alpha]-=1
            else:
                return False
        for i in mapS:
            if mapS[i]!=0:
                return False
        return True

        

