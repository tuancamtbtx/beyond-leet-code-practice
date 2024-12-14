class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for char in s:
            # when char is close bracket , pop value from stack and check it
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            # when char is open bracket add to stack
            else:
                stack.append(char)
        return not stack


def main():
    solution = Solution()
    s = "[{(})]"
    result = solution.isValid(s)
    print('result', result)
if __name__ == "__main__":
    main()