class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == '+':
                stack.append(stack.pop() + stack.pop())

            elif char == '-':
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(operand1 - operand2)

            elif char == '*':
                stack.append(stack.pop() * stack.pop())

            elif char == '/':
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(int(operand1 / operand2))

            else:
                stack.append(int(char))
            
        return stack[-1]
