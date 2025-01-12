def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
arr = list(map(int, input("Enter a list of integers (comma-separated): ").split(',')))
sorted_arr = bubble_sort(arr)
print("Sorted list:", sorted_arr)
