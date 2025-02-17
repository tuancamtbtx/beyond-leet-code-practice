The two-pointer technique is a common approach used to solve problems involving arrays or linked lists. This technique is particularly useful for problems that require finding pairs, triplets, or other combinations of elements that meet certain criteria. It is often used to optimize problems that would otherwise require nested loops, thus reducing time complexity.

### Steps to Solve Problems Using the Two-Pointer Technique

1. **Understand the Problem:** Determine if the problem can be solved using the two-pointer technique. Look for requirements involving pairs, triplets, or specific order constraints.

2. **Sort the Array (if necessary):** Many two-pointer problems require the array to be sorted. If the problem doesn't specify that the input is sorted, you may need to sort it first.

3. **Initialize Pointers:** Use two pointers to represent positions in the array. Common setups include:
   - **Start and End Pointers:** One pointer starts at the beginning of the array, and the other starts at the end.
   - **Adjacent Pointers:** Both pointers start at the beginning or end and move in tandem.

4. **Move Pointers Based on Conditions:** Adjust the pointers based on the problem's requirements. Typically, you move one or both pointers until you find a solution or exhaust the possibilities.

5. **Check and Update Results:** As you move the pointers, check if the current elements meet the criteria and update the result accordingly.

6. **Consider Edge Cases:** Handle special cases such as empty input, arrays with only one element, or cases where no solution exists.

### Example Problem: Two Sum II - Input Array Is Sorted

Let's solve a problem where we need to find two numbers in a sorted array that add up to a specific target.

**Problem Statement:**
Given a sorted array of integers and a target sum, find the indices of the two numbers such that they add up to the target. The solution should return the indices as a list `[index1, index2]`, where `index1 < index2`.

**Solution Using Two Pointers:**

```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [left + 1, right + 1]  # Return 1-based indices
        elif current_sum < target:
            left += 1  # Move the left pointer to the right
        else:
            right -= 1  # Move the right pointer to the left

    return []  # Return an empty list if no solution is found

# Example usage
arr = [2, 3, 4, 7, 11]
target = 9
print(two_sum_sorted(arr, target))  # Output: [1, 3] (2 + 7 = 9)
```

### Explanation:

- **Initialize Pointers:** We use `left` and `right` pointers to start at the beginning and end of the array, respectively.
- **Calculate Current Sum:** We calculate the sum of the elements at the `left` and `right` pointers.
- **Adjust Pointers:** 
  - If the sum equals the target, return the indices (adjusted for 1-based indexing).
  - If the sum is less than the target, move the `left` pointer to the right to increase the sum.
  - If the sum is greater than the target, move the `right` pointer to the left to decrease the sum.
- **Return Result:** If no valid pair is found, return an empty list.

### Tips for Using the Two-Pointer Technique:

- **Sorting:** If the array is not sorted and sorting is feasible, consider sorting it first to simplify the problem.
- **Multiple Solutions:** Be aware of whether the problem requires you to find all solutions or just one.
- **Avoid Overlapping:** Ensure that the pointers do not overlap unless the problem allows it.
- **Practice:** Solve various problems to become familiar with different ways to apply the two-pointer technique.

By understanding and practicing the two-pointer technique, you can efficiently solve a wide range of problems involving arrays and linked lists.