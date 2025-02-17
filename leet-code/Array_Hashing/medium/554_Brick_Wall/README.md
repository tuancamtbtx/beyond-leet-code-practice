There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height (i.e., one unit) but they can be of different widths. The total width of each row is the same.

Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Given the 2D array wall that contains the information about the wall, return the minimum number of crossed bricks after drawing such a vertical line.
Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
Output: 2
Example 2:

Input: wall = [[1],[1],[1]]
Output: 3
 

Constraints:

n == wall.length
1 <= n <= 104
1 <= wall[i].length <= 104
1 <= sum(wall[i].length) <= 2 * 104
sum(wall[i]) is the same for each row i.
1 <= wall[i][j] <= 231 - 1

# Calulate BigO:
To determine the time complexity (Big O notation) of the `leastBricks` function in the given code, we need to analyze the operations involved in the algorithm.

### Code Explanation:
1. **Initialization**: A dictionary `gap_count` is initialized with a single entry `{0: 0}`. This dictionary is used to count the number of times a gap (where a brick ends and another brick starts) occurs at a particular position across all rows of the wall.

2. **Outer Loop**: The outer loop iterates over each row `i` in the `wall`. If `wall` has `n` rows, this loop runs `n` times.

3. **Inner Loop**: For each row `i`, the inner loop iterates over the bricks in the row, except for the last brick (`i[:-1]`). If a row has `m` bricks, this loop runs `m-1` times. The reason the last brick is excluded is that a gap at the end of the row is not useful for minimizing the number of bricks crossed.

4. **Operations in Inner Loop**: For each brick in the inner loop:
   - The current brick's width is added to `total`, which keeps track of the cumulative width from the beginning of the row.
   - The cumulative width `total` is used as a key in the `gap_count` dictionary to count the occurrence of gaps at that position. This involves a dictionary `get` and an assignment operation.

5. **Final Calculation**: After processing all rows, the function calculates the maximum number of gaps that can be aligned vertically across the wall (`max(gap_count.values())`). The result is computed as the total number of rows minus this maximum gap count, which represents the minimum number of bricks crossed.

### Time Complexity Analysis:
- **Outer Loop**: Runs `n` times, where `n` is the number of rows in the wall.
- **Inner Loop**: For each row, runs `m-1` times, where `m` is the average number of bricks per row. In the worst case, this is proportional to the length of the longest row, which we can denote as `m_max`.
- **Dictionary Operations**: The operations on the dictionary, such as `get` and assignment, are average O(1) operations.

Combining these, the overall time complexity of the function is O(n * m_max), where `n` is the number of rows and `m_max` is the maximum number of bricks in any row. This is because for each of the `n` rows, we perform operations proportional to the number of bricks in that row (except the last brick).

### Space Complexity:
The space complexity is primarily determined by the `gap_count` dictionary, which can hold at most `n * m_max` entries in the worst case (if every brick ends at a unique position). However, practically, it is limited by the number of unique gap positions, which is generally much smaller than `n * m_max`. Thus, the space complexity is O(n * m_max) in the worst case.