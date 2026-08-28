class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        opera = {'+','-','/','*'}
        op = tokens.pop()
        match op:
            case '+':
                if tokens[-1] in opera:
                    num1 = self.evalRPN(tokens)
                else:
                    num1 = int(tokens.pop())                
                if tokens[-1] in opera:
                    num2 = self.evalRPN(tokens)
                else:
                    num2 = int(tokens.pop())
                
                return num2 + num1
                
            case '-':
                if tokens[-1] in opera:
                    num1 = self.evalRPN(tokens)
                else:
                    num1 = int(tokens.pop())
                if tokens[-1] in opera:
                    num2 = self.evalRPN(tokens)
                else:
                    num2 = int(tokens.pop())
                return num2 - num1
            case '*':
                if tokens[-1] in opera:
                    num1 = self.evalRPN(tokens)
                else:
                    num1 = int(tokens.pop())
                 
                if tokens[-1] in opera:
                    num2 = self.evalRPN(tokens)
                else:
                    num2 = int(tokens.pop())
                
                return num2 * num1
            case '/':
                if tokens[-1] in opera:
                    num1 = self.evalRPN(tokens)
                else:
                    num1 = int(tokens.pop())
         
                if tokens[-1] in opera:
                    num2 = self.evalRPN(tokens)
                else:
                    num2 = int(tokens.pop())
                
                return int(num2/num1)
            case _:
                return int(op)
