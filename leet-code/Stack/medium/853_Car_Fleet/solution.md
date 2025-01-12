To solve the car fleet problem using a stack, we can utilize the stack data structure to keep track of the times it takes for each car to reach the target. The stack will help us manage the merging of cars into fleets efficiently.

Here's a step-by-step approach using a stack:

1. **Calculate Time to Target:** For each car, calculate the time it will take to reach the target using the formula:
   \[
   \text{time}[i] = \frac{\text{target} - \text{position}[i]}{\text{speed}[i]}
   \]

2. **Sort Cars by Starting Position:** Sort the cars by their starting positions in descending order. This ensures that we process the cars from the one closest to the target to the one farthest from the target.

3. **Use a Stack to Track Fleets:** Initialize an empty stack. As you iterate through the sorted list of cars:
   - Push the time it takes for each car to reach the target onto the stack.
   - If the current car takes less time than the car at the top of the stack, it means this car will merge into the fleet of the car on top of the stack.

4. **Count Fleets:** The size of the stack at the end of the iteration represents the number of distinct fleets that will reach the target.

Here's the Python implementation:

```python
def carFleet(target, position, speed):
    # Calculate time to reach the target for each car
    times = [(target - p) / s for p, s in zip(position, speed)]
    
    # Pair position and times, and sort by position in descending order
    cars = sorted(zip(position, times), reverse=True)
    print(times)
    print(cars)
    # Use a stack to determine the number of fleets
    stack = []
    for _, time in cars:
        # If the stack is empty or the current car takes more time,
        # it forms a new fleet
        if not stack or time > stack[-1]:
            stack.append(time)
    
    # The number of fleets is the size of the stack
    return len(stack)

# Example usage:
# target = 12
# position = [10, 8, 0, 5, 3]
# speed = [2, 4, 1, 1, 3]
# print(carFleet(target, position, speed))  # Output: 3
```

### Explanation:

- **Sorting by Position:** The cars are sorted by their starting positions in descending order, allowing us to process them from closest to the target to farthest.

- **Stack Usage:** As we iterate over the sorted list, we push the time it takes for each car to reach the target onto the stack. If a car cannot catch up to the fleet represented by the top of the stack, it forms a new fleet, and we push its time onto the stack.

- **Counting Fleets:** The number of fleets is determined by the number of distinct times on the stack, representing different fleets that reach the target independently.