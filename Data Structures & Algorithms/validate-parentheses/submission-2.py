class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        corsp = {
            ']':'[',
            ')':'(',
           '}':'{'
        }
        for ch in s:
            if ch in corsp and len(stack)>0:
                if stack[-1] == corsp[ch]:
                    stack.pop()
                    continue
            stack.append(ch)

        return len(stack)==0

