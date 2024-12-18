Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100

**Solution:**
To solve this problem, you can use a stack to efficiently find the number of days until a warmer temperature. The stack will store indices of the `temperatures` array, and we'll use it to keep track of the indices of temperatures that haven't yet found a warmer day.

Here's how you can implement this:

```python
def dailyTemperatures(temperatures):
    n = len(temperatures)
    answer = [0] * n  # Initialize the answer array with zeros
    stack = []  # This will store indices of the temperatures array

    for i in range(n):
        # While the stack is not empty and the current temperature is greater than
        # the temperature at the index stored at the top of the stack
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_index = stack.pop()  # Get the index of the previous day
            answer[prev_index] = i - prev_index  # Calculate the number of days
        stack.append(i)  # Push the current index onto the stack

    return answer

# Example usage:
temperatures1 = [73, 74, 75, 71, 69, 72, 76, 73]
output1 = dailyTemperatures(temperatures1)
print("Output for temperatures = [73, 74, 75, 71, 69, 72, 76, 73]:", output1)

temperatures2 = [30, 40, 50, 60]
output2 = dailyTemperatures(temperatures2)
print("Output for temperatures = [30, 40, 50, 60]:", output2)

temperatures3 = [30, 60, 90]
output3 = dailyTemperatures(temperatures3)
print("Output for temperatures = [30, 60, 90]:", output3)
```

### Explanation:
- We initialize an `answer` array of the same length as `temperatures`, filled with zeros.
- We use a stack to keep track of indices of temperatures that have not yet found a warmer day.
- We iterate through the `temperatures` array. For each temperature, we check if it is warmer than the temperature at the index stored at the top of the stack.
- If it is warmer, we pop the index from the stack, calculate the difference between the current index and the popped index, and store this difference in the `answer` array at the popped index.
- We then push the current index onto the stack.
- This approach ensures that each index is pushed and popped from the stack at most once, resulting in an O(n) time complexity, which is efficient for the given constraints.