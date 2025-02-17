When dealing with problems that involve arrays and hashing, the goal is often to use hash-based data structures to efficiently solve problems related to searching, counting, or organizing data. Here are some general steps and strategies you can use to tackle such problems, along with examples to illustrate these techniques.

### General Approach

1. **Identify the Problem Type:** Determine what kind of problem you're dealing with. Common problems include finding duplicates, counting occurrences, checking for a particular condition, or finding intersections/unions.

2. **Choose the Right Data Structure:** Depending on the problem, decide whether to use a hash set or a hash map (dictionary).
   - **Hash Set:** Useful for checking the existence of elements or removing duplicates.
   - **Hash Map (Dictionary):** Useful for counting occurrences or storing key-value pairs.

3. **Initialize the Data Structure:** Set up an empty hash set or hash map to store data as you iterate through the array.

4. **Process the Array:** Loop through the array, updating the hash data structure based on the problem's requirements.

5. **Extract Results:** Use the data stored in the hash data structure to derive the solution to the problem.

6. **Handle Edge Cases:** Consider special cases, such as empty arrays or arrays with all identical elements.

### Examples

#### Example 1: Finding Duplicates

**Problem Statement:** Given an array of integers, determine if there are any duplicates.

**Solution Using Hash Set:**

```python
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Example usage
nums = [1, 2, 3, 4, 5, 1]
print(contains_duplicate(nums))  # Output: True
```

**Explanation:** 
- We use a hash set `seen` to track elements we've encountered.
- As we iterate through `nums`, we check if the current number is already in `seen`.
- If it is, we return `True` (found a duplicate). Otherwise, we add the number to `seen`.

#### Example 2: Counting Element Frequencies

**Problem Statement:** Given an array of integers, count the frequency of each element.

**Solution Using Hash Map:**

```python
def count_frequencies(nums):
    frequency_map = {}
    for num in nums:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1
    return frequency_map

# Example usage
nums = [1, 2, 2, 3, 3, 3]
print(count_frequencies(nums))  # Output: {1: 1, 2: 2, 3: 3}
```

**Explanation:**
- Use a hash map `frequency_map` to store each number as a key and its count as the value.
- Iterate through `nums`, updating the count for each number.

#### Example 3: Intersection of Two Arrays

**Problem Statement:** Given two arrays, find their intersection.

**Solution Using Hash Set:**

```python
def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return list(set1 & set2)

# Example usage
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection(nums1, nums2))  # Output: [2]
```

**Explanation:**
- Convert both arrays to sets to eliminate duplicates and use set intersection to find common elements.
- The result is converted back to a list.

### Tips for Solving Array and Hashing Problems:

- **Efficiency:** Hashing provides average O(1) time complexity for insertions and lookups, making it efficient for large datasets.
- **Memory Usage:** Be mindful of the space complexity, as hash-based structures require additional memory.
- **Practice:** Solve various problems to become familiar with using hash sets and hash maps effectively.
- **Edge Cases:** Always consider edge cases, such as empty arrays or arrays with all identical elements, to ensure your solution is robust.

By understanding and practicing these techniques, you can effectively solve a wide range of problems involving arrays and hashing.