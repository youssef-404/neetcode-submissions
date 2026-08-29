class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f'{len(s)}@{s}' for s in strs)
    
    def decode(self, s: str) -> List[str]:
        left = 0
        right = 1
        strs = []
        while right < len(s):
            if s[right]== "@":
                size = int(s[left:right])
                word = s[right+1:right+1+size]
                strs.append(word)
                left = right+1+size
                right = right+1+size
            
            right+=1
        return strs