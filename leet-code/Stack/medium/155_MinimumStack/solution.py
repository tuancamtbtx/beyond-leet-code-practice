class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        

    def pop(self) -> None:
        if self.stack:
            top_val = self.stack.pop()
            if top_val == self.min_stack[-1]:
                self.min_stack.pop()
        

    def top(self) -> int:
        self.stack[-1] if self.stack else None
        

    def getMin(self) -> int:
        self.min_stack[-1] if self.min_stack else None
        

def main():
    stack = [1,2,4]
    print(stack[-1])
if __name__ == "__main__":
    main()