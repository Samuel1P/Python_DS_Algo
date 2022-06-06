"""
Insertion sort
Big O: O(n²) but on most common cases it O(n)
"""

sample_data = list(range(50,45,-1)) # [50, 49, 48, 47, 46]
#sample_data = list(range(45,50)) # [45, 46, 47, 48, 49]

print("input: ", sample_data)
def insertion_sort(list_data):
    list_len = len(list_data)
    for i in range(1, list_len):
        temp = list_data[i]
        j = i-1
        while temp < list_data[j] and j > -1:
            list_data[j], list_data[j+1] = temp, list_data[j]
            j -= 1

    return list_data

insertion_sort(sample_data)
print("output: ", sample_data)