def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
arr = list(map(int, input("Enter a list of integers (comma-separated): ").split(',')))
sorted_arr = quick_sort(arr)
print("Sorted list:", sorted_arr)
