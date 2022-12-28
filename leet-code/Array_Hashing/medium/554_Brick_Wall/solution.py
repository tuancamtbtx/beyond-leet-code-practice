class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        gap_count = { 0: 0}
        for i in wall:
            total = 0
            for j in i[:-1]:
                total += j
                gap_count[total] = 1 + gap_count.get(total, 0)
        return len(wall) - max(gap_count.values())        
def main():
    solution = Solution()
    wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
    result = solution.leastBricks(wall)
    print('result',result)
    
if __name__ == "__main__":
    main()