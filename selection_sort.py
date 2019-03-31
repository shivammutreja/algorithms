from __init__ import time_elapsed, arr

@time_elapsed
def selection_sort(a, length, iteration):
    for i in range(length):
        #if iteration == 0:
        #    break
        _min = i
        for j in range(i+1, length):
            if a[j]<a[_min]:
                _min = j
        a[_min], a[i] = a[i], a[_min]
        #iteration -= 1
    return a

#arr = [88,18,31,96,78,69,86,15,5,66,35,68,14,42,83,69,25,17,92,38,44,48,22,36,56,33,66,15,17,80]

print(selection_sort(arr, len(arr), 2))
