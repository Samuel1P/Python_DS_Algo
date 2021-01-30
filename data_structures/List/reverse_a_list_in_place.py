# This method reverses list without taking additional space.
# Time compexity is O(N) Linear as it goes through every item to swap

def reverse_list(arr):
    # starting index of list
    start = 0
    # last index of the list
    end = len(arr)-1

    # swap last and first index item
    # increment first and decrement last until middle is reached
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start=start+1
        end=end-1
    return arr

test_list1 = [1,2,3,4,5]
test_list2 = [1,2]
test_list3 = []

print (reverse_list(test_list1))  # [5, 4, 3, 2, 1]
print (reverse_list(test_list2))  # [2, 1]
print (reverse_list(test_list3))  # []