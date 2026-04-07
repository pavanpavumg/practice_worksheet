def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = list(map(int, input("Enter numbers: ").split()))
bubble_sort(arr)
print("Sorted:", arr)

x = int(input("Enter element to search: "))
pos = binary_search(arr, x)
print(f"Element {x} found at index {pos}." if pos != -1 else f"{x} not found.")