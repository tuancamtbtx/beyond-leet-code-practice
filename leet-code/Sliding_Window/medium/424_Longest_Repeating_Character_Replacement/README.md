You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

# Resolve:
This problem can be solved using the "sliding window" technique, which is a common approach for handling problems involving substrings. The key idea here is to maintain a window that represents the current substring being considered, and adjust the window size and position as needed to ensure that the substring can be transformed into a string of repeating characters with at most `k` changes.

### Approach

1. **Sliding Window**: Use two pointers to represent the current window of characters. The window expands and contracts to maintain the property that it can be transformed into a substring of repeating characters with at most `k` changes.

2. **Character Frequency Count**: Use a dictionary to keep track of the frequency of each character within the current window.

3. **Max Frequency**: Keep track of the maximum frequency of any character within the current window. This helps determine if the window can be transformed into a substring of repeating characters with the allowed number of changes.

4. **Adjust Window**: If the size of the current window minus the maximum frequency of any character is greater than `k`, move the start of the window to the right to reduce the window size.

5. **Calculate Maximum Length**: Continuously update the maximum length of the substring that can be transformed into repeating characters.

### Python Solution

```python
def characterReplacement(s, k):
    # Dictionary to store the frequency of characters in the current window
    char_count = {}
    # Initialize the start of the window and the maximum length
    max_length = 0
    start = 0
    max_freq = 0

    for end in range(len(s)):
        char = s[end]
        # Update the frequency of the current character
        char_count[char] = char_count.get(char, 0) + 1
        # Update the maximum frequency in the current window
        max_freq = max(max_freq, char_count[char])

        # Check if the current window is valid
        if (end - start + 1) - max_freq > k:
            # If not valid, reduce the window size from the left
            left_char = s[start]
            char_count[left_char] -= 1
            start += 1

        # Update the maximum length of the valid window
        max_length = max(max_length, end - start + 1)

    return max_length

# Example usage
s1 = "ABAB"
k1 = 2
print(characterReplacement(s1, k1))  # Output: 4

s2 = "AABABBA"
k2 = 1
print(characterReplacement(s2, k2))  # Output: 4
```

### Explanation

- **char_count**: A dictionary to keep track of the frequency of each character within the current window.
- **max_freq**: The maximum frequency of any character within the current window.
- **Adjust Window**: If the number of characters that need to be changed to make the current window valid exceeds `k`, move the start of the window to the right.
- **Update max_length**: After processing each character, update the maximum length of the valid window.

This solution efficiently finds the length of the longest substring that can be transformed into repeating characters in O(n) time, where n is the length of the string.