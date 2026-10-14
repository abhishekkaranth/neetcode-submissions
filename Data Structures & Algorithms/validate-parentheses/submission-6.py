class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        pairs = {'(': ')', '[': ']', '{': '}'}
        for char in s:
            if char in pairs.keys():
                stack.append(char)
            else:
                if stack and pairs[stack[-1]] == char:
                    stack.pop()
                else:
                    return False

        return not stack
