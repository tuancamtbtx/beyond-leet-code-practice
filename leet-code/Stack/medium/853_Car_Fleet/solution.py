from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [(target - p)/ s for p, s, in (zip(position, speed))]
        cars = sorted(zip(position, times), reverse = True)

        stack = []
        for _, time in cars: 
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)

def main():
    solution = Solution()
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    result = solution.carFleet(target, position, speed)
    print(result)
if __name__ == "__main__":
    main()