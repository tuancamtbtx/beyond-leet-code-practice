class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        num_rows = len(matrix)
        num_cols = len(matrix[0]) if num_rows > 0 else 0
        n = num_rows * num_cols
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            row = mid // num_cols
            col = mid % num_cols
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
        
def main():
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    solution = Solution()
    result = solution.searchMatrix(matrix, target)
    print(result)
if __name__ == "__main__":
    main()