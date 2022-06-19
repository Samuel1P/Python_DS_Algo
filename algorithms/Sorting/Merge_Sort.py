"""
Merge sort
Time Big O: O(n log n)
Space : O(n)
"""

sample_data =  [50, 49, 48, 47, 46, 1, 0]
#sample_data = list(range(45,50)) # [45, 46, 47, 48, 49]

print("input: ", sample_data)
def merge(l1, l2):
    combined = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            combined.append(l1[i])
            i += 1
        else:
            combined.append(l2[j])
            j += 1
    if i < len(l1):
        combined.extend(l1[i:])
    else:
        combined.extend(l2[j:])
    return combined

def merge_sort(sample_list):
    if len(sample_list) == 1:
        return sample_list
    mid = len(sample_list)//2
    left = sample_list[:mid]
    right = sample_list[mid:]
    return merge(merge_sort(left), merge_sort(right))
    

output_data = merge_sort(sample_data)
print("output: ", output_data)