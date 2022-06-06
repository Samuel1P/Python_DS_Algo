"""
Selection Sort
Big O: O(n²) 
In Place solution.
"""

sample_data = list(range(50,45,-1)) # [50, 49, 48, 47, 46]
#sample_data = list(range(45,50)) # [45, 46, 47, 48, 49]

def selection_sort(list_data):
    global cycle
    list_len = len(list_data)
    for outer_indx in range(list_len-1):
        min_index = outer_indx
        for inner_indx in range(outer_indx+1, list_len):
            if list_data[min_index] > list_data[inner_indx]:
                min_index = inner_indx
        if min_index != outer_indx:
            list_data[outer_indx], list_data[min_index] = list_data[min_index], list_data[outer_indx]
    return list_data

selection_sort(sample_data)
print("output: ", sample_data)