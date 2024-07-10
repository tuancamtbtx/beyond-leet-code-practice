from typing import Any


class Memoization:
    def __init__(self) -> None:
        pass
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("Calling Memoization")

def main():
    print("Hello World")
    mem = Memoization()
    print(mem(1, 2, 3))

if __name__ == "__main__":
    main()