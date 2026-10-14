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
                if not stack:
                    return False
                latest_bracket = stack.pop()
                if char != pairs[latest_bracket]:
                    return False

        return True if not stack else False
