from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []
        def backtrack(stack, result, left, right):
            if len(stack) == 2 * n:
                result.append("".join(stack))
                return
            if left < n:
                stack.append("(")
                backtrack(stack, result, left + 1, right)
                stack.pop()
            if right < left:
                stack.append(")")
                backtrack(stack, result, left, right + 1)
                stack.pop()
            print(left, right, stack)
        backtrack(stack, result, 0, 0)
        return result


def main():
    solution = Solution()
    n = 3
    out = solution.generateParenthesis(n)
    print(out)
if __name__ == "__main__":
    main()