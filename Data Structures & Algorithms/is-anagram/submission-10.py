class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}

        for elm in s:
            s_map[elm] = s_map.get(elm,0) + 1
        for elm in t:
            t_map[elm] = t_map.get(elm,0) + 1
        
        for elm in s:
            if s_map.get(elm) != t_map.get(elm):
                return False
        return True