class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesisMap = { ')' : '(',
                          '}' : '{',
                          ']' : '[' }
        
        for char in s:
            if char in parenthesisMap:
                if stack and stack[-1] == parenthesisMap[char]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(char)

        return True if not stack else False