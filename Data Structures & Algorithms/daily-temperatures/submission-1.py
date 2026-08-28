class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i,v in enumerate(temperatures):
            while stack and v> stack[-1][-1]:
                last = stack.pop()
                res[last[0]] = i - last[0]
            stack.append((i,v))
        return res