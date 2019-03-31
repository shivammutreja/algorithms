from __init__ import time_elapsed, arr

@time_elapsed
def insertion_sort(arr): 
    for i in range(len(arr)):
        temp = arr[i]
        j = i
        while (j>0 and temp<arr[j-1]):
            arr[j] = arr[j-1]
            j -= 1
            arr[j] = temp
        
    return arr

print(insertion_sort(arr))
