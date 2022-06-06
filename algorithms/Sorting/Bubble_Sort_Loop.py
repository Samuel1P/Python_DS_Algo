"""
Bubble sort
Big O: O(n²) - This is due to the nested for loop.
"""
sample_data = list(range(50,45,-1))
print("input: ", sample_data)

def bubble_sort(list_data):
    list_len = len(list_data)
    for dec_len in range(list_len-1, 0, -1):
        for i in range(dec_len):
            if list_data[i] > list_data[i+1]:
                list_data[i], list_data[i+1] = list_data[i+1], list_data[i]
    return (list_data)
    
bubble_sort(sample_data)
print("output: ", sample_data)