class Solution:
    def isValid(self, s):
        matching = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            if char in matching:
                top_element = stack.pop() if stack else '#'
                if matching[char] != top_element:
                    return False
            else:
                stack.append(char)
                
        return len(stack) == 0