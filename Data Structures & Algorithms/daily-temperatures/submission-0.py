class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)


        for idex, val in enumerate(temperatures):
            i = idex +1
            while i<len(temperatures):
                if val<temperatures[i]:
                    res[idex] = i-idex
                    break
                i+=1
        return res