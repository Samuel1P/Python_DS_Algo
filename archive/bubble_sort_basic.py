#Easy way to sort integers in a list but performance wise bad
#

arr_ = [3,1,4,5,3,6,7,3,2,1]

def bubble_sort(arr):
    size = len(arr)
    count = 0
    for i in range(0,size-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            count = count + 1
    if count == 0:
        return arr
    else:
        return bubble_sort(arr)

print(bubble_sort(arr_))
