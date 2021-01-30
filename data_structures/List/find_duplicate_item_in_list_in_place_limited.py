# find duplicate item in a list
# this method will not utilize any extra space
# limitations:
# 1. all integers have to be positive.
# 2. all the integer items are smaller than the size of the list.

arr = [5, 4, 3, 2, 1, 5, 1, 3]

def find_dups(arr):
    repetition = []
    for i in arr:
        # i is the item iterating
        # see if the i'th item in arr list is positive (we're not checking if 'i' is positive)
        if arr[abs(i)] >= 0:
            # swap the items sign
            arr[abs(i)] = -arr[abs(i)]
        else:
            # if item is not positive it is duplicate
            repetition.append(abs(i))
    print (f"repetitions - {repetition}")

find_dups(arr)