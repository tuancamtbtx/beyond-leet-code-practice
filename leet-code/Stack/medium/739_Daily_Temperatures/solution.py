from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        results = [0] * n
        stack = []
        for i in range (n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                previous_index = stack.pop()
                results[previous_index] = i - previous_index
            stack.append(i)
        return results


def main():
    solution = Solution()
    temperatures = [73,74,75,71,69,72,76,73]
    result = solution.dailyTemperatures(temperatures)
    print(result)
if __name__ == "__main__":
    main()