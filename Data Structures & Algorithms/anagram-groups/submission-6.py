class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashed = defaultdict(list)

        for s in strs:
            alphabets= [0]*26
            for ch in s:
               alphabets[ord(ch)-ord('a')]+=1 
            hashed[tuple(alphabets)].append(s)

        return list(hashed.values())