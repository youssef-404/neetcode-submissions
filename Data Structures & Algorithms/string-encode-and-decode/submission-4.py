class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+=f'é{s}'
        return res
    
    def decode(self, s: str) -> List[str]:
        return s.split("é")[1:]