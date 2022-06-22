"""
Quick sort : In-place solution

"""
from functools import partial

sample_data =  [4,6,1,7,3,2,5]

print("input: ", sample_data)

def pivot(my_list, pivot_index, last_index):
    swap = pivot_index
    for i in range(pivot_index+1, last_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap += 1
            my_list[i], my_list[swap] = my_list[swap], my_list[i]
    my_list[pivot_index], my_list[swap] = my_list[swap], my_list[pivot_index]
    return swap
    


def quick_sort(sample_list, left, right):
    if left < right:
        pv = pivot(sample_list, left, right)
        quick_sort(sample_list, left, pv-1)
        quick_sort(sample_list, pv+1, right)
    return sample_list

last_index = len(sample_data) - 1
_quick_sort = partial(quick_sort, left=0 , right=last_index)
output_data = _quick_sort(sample_data)
print("output: ", sample_data )