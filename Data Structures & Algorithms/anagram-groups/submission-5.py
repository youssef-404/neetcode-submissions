class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashed = {}

        for s in strs:
            alphabets= [0]*26
            for ch in s:
               alphabets[ord(ch)-ord('a')]+=1 
            if tuple(alphabets) not in hashed:
                hashed[tuple(alphabets)] = []
            hashed[tuple(alphabets)].append(s)

        res = []
        for i in hashed:
            res.append(list(hashed[i]))
        return res