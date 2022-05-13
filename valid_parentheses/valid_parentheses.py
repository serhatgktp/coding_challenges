class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        map = {')':'(', ']':'[', '}':'{'}
        
        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)
            elif ch == ')' or ch == ']' or ch == '}':
                if stack[-1] != map[ch]:
                    return False
                else:
                    stack.pop()
        
        return (len(stack) == 0)