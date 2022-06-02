"""
Bubble sort
Big O: # O(n²) - ???? Need to check
"""

sample_data = list(range(50,45,-1))
cycle = 0
print("input: ", sample_data)


def bubble_sort(list_data):
    global cycle
    list_len = len(list_data)
    count = 0
    for i in range(0, list_len-1):
        cycle += 1
        if list_data[i] > list_data[i+1]:
            list_data[i], list_data[i+1] = list_data[i+1], list_data[i]
            count += 1
    if count == 0 :
        return list_data
    return bubble_sort(list_data)
    
bubble_sort(sample_data)
print("output: ", sample_data)
print("n: ", cycle)
