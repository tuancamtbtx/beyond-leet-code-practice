from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for char in tokens:
            if char in operators:
                first = stack.pop()
                second = stack.pop()
                if char == '+':
                    stack.append(second + first)
                elif char == '-':
                    stack.append(second - first)
                elif char == '*':
                    stack.append(second * first)
                else:
                    stack.append(int(second / first))
            else:
                stack.append(int(char))
        return stack[-1]

def main():
    solution = Solution()
    tokens = ["2", "1", "+", "3", "*"]
    out = solution.evalRPN(tokens)
    print(out)
if __name__ == "__main__":
    main()