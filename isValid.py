class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(', ']':'[', '}':'{'}
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if stack and stack[-1] == mapping[char]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
    

a = "[{}]"
c = "}{"
d = "[ad{cf}]"
b = Solution()
h = b.isValid(d)
print(h) 
    