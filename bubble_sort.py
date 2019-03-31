#import datetime

from __init__ import time_elapsed, arr

@time_elapsed
def bubble_sort(arr):
    for x in range(len(arr)-1):
		#(x-1) is for ignoring comparisons of elements which have already been compared in earlier iterations
        for i in range(len(arr)-x-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    return arr

#arr = [7,5,2,4,9,1,0]
print(bubble_sort(arr))

