from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        print(k)



def main():
    solution = Solution()
    piles = [3,6,7,11]
    h = 8
    result = solution.minEatingSpeed(piles=piles, h=h)
    print(result)

if __name__ == '__main__':
    main()