Memoization is a technique used to optimize functions by storing the results of expensive function calls and returning the cached result when the same inputs occur again. In Python, the `functools.lru_cache` decorator provides a convenient way to implement memoization.

However, in the context of the "good days to rob the bank" problem, memoization using `lru_cache` is not directly applicable because the problem involves iterating over an array and does not involve recursive function calls or repeated calculations with the same inputs.

That said, I can demonstrate how `lru_cache` works with a simple example of a recursive function where memoization is beneficial, such as calculating Fibonacci numbers:

```python
from functools import lru_cache

@lru_cache(maxsize=None)  # Cache with unlimited size
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
print(fibonacci(10))  # Output: 55
```

### Explanation of `lru_cache`:

- **Decorator:** `@lru_cache` is a decorator that can be applied to a function to enable memoization.
- **maxsize:** The `maxsize` parameter determines the number of results to cache. If set to `None`, the cache can grow without bound.
- **Functionality:** When `fibonacci(n)` is called, the result is stored in the cache. Subsequent calls with the same `n` will return the cached result, avoiding redundant calculations.

### Application to the Bank Robbing Problem:

For the bank robbing problem, since it involves linear iteration and does not have overlapping subproblems that would benefit from memoization, using `lru_cache` is not suitable. The algorithm is already efficient with a time complexity of O(n), and memoization would not provide additional benefits in this context.

If you have a different problem or function that could benefit from memoization, feel free to provide more details, and I can help demonstrate how to apply `lru_cache` effectively.