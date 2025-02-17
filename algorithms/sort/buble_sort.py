def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the array
    for i in range(n):
        # Initialize a flag to detect any swaps
        swapped = False
        # Last i elements are already sorted, so we can skip them
        for j in range(0, n - i - 1):
            # Compare the current element with the next
            if arr[j] > arr[j + 1]:
                # Swap if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no elements were swapped, the array is already sorted
        if not swapped:
            break

# Example usage
if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", data)
    bubble_sort(data)
    print("Sorted array:", data)