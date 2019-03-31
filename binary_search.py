from __init__ import time_elapsed, arr


@time_elapsed
def binary_search(arr, low, high, key):
    while (low <= high):
        mid = (low+high) >> 1
        if arr[mid] < key:
            low = mid+1
        elif arr[mid] > key:
            high = mid-1
        else:
            return mid
    return False

print(binary_search(sorted(arr), 0, len(arr)-1, 83))
