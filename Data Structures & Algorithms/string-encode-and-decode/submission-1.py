class Solution:

    def encode(self, strs: List[str]) -> str:
        result= ''
        for s in strs:
            result+=f"{len(s)}@{s}"
        return result
    def decode(self, s: str) -> List[str]:
        i = 0
        decode = []
        while i<len(s):
            k = i
            delm = s[k]
            while delm != '@':
                k+=1
                delm = s[k]
            j = int(s[i:k]) + 1
            decode.append(s[k+1:k+j])
            i=j+k
   
        return decode