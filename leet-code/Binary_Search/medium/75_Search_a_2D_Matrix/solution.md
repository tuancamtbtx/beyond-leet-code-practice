You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

The line `row = mid // num_cols` is part of a technique used to perform a binary search on a 2D matrix that is treated as a flattened 1D array. This approach is often used when the matrix is stored in memory as a 2D list or array, but you want to leverage the properties of binary search to efficiently locate an element.

Here's a breakdown of how this works:

### Context

Suppose you have a 2D matrix, and you want to perform a binary search on it. The matrix is typically represented as a list of lists, and binary search is naturally suited for 1D sorted arrays. To apply binary search on a 2D matrix, you can imagine the matrix as a single flattened 1D array.

### Explanation

1. **Flattening the Matrix Conceptually:**
   - Imagine the matrix as a single list where the first row is followed by the second row, and so on.
   - For example, a 3x3 matrix:
     ```
     [
       [1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]
     ]
     ```
     Conceptually becomes:
     ```
     [1, 2, 3, 4, 5, 6, 7, 8, 9]
     ```

2. **Mapping 1D Index to 2D Indices:**
   - If you have an index `mid` in this conceptual 1D array, you can find the corresponding row and column in the original 2D matrix.
   - `row = mid // num_cols`: This calculates the row index by integer division of `mid` by the number of columns (`num_cols`). It gives the number of complete rows before the `mid` index.
   - `col = mid % num_cols`: This calculates the column index by taking the remainder of `mid` divided by the number of columns. It gives the position within the row.

### Example

Consider a 3x3 matrix with `num_cols = 3`:

- If `mid = 4`, then:
  - `row = 4 // 3 = 1` (second row, since indexing starts from 0)
  - `col = 4 % 3 = 1` (second column)
- The element at `mid = 4` corresponds to `matrix[1][1]`, which is `5` in the given example.

This approach allows you to perform binary search on a 2D matrix by treating it as a 1D array and mapping indices accordingly. This is particularly useful when the matrix is sorted in a row-wise and column-wise manner.