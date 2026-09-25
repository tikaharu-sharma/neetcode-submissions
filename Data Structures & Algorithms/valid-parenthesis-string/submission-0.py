class Solution:
    def checkValidString(self, s: str) -> bool:
        stack_open_bracket = []
        stack_star = []

        for i, char in enumerate(s):
            if char == "(":
                stack_open_bracket.append(i)
            elif char == "*":
                stack_star.append(i)
            else:
                if not stack_open_bracket and not stack_star:
                    return False
                if not stack_open_bracket:
                    stack_star.pop()
                elif not stack_star:
                    stack_open_bracket.pop()
                else:
                    stack_open_bracket.pop()
        while stack_open_bracket and stack_star:
            if stack_open_bracket[-1] > stack_star[-1]:
                return False
            stack_open_bracket.pop()
            stack_star.pop()
        
        return not stack_open_bracket

