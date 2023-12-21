# Stack and Queue

## Stack
### Overview
A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. Elements are added and removed from the same end, known as the top of the stack.

### Operations
- **Push**: Adds an element to the top of the stack.
- **Pop**: Removes and returns the element from the top of the stack.
- **Peek (or Top)**: Returns the element at the top of the stack without removing it.
- **isEmpty**: Checks if the stack is empty.
- **size**: Returns the number of elements in the stack.

### Usage
Stacks are used in various applications, including:
- Function call management in programming language compilers
- Expression evaluation and syntax parsing
- Undo functionality in text editors
- Backtracking algorithms in maze-solving problems

### Example
```javascript
// Sample code demonstrating the implementation of a stack in JavaScript
class Stack {
  constructor() {
    this.items = [];
  }

  push(element) {
    this.items.push(element);
  }

  pop() {
    if (this.items.length === 0) {
      return "Underflow";
    }
    return this.items.pop();
  }

  peek() {
    return this.items[this.items.length - 1];
  }

  isEmpty() {
    return this.items.length === 0;
  }

  size() {
    return this.items.length;
  }
}