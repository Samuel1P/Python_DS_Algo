# this code will search for a integer in a sorted list using while loop

arr_ = [1, 1, 2, 3, 3, 3, 4, 5, 6, 7]


def binary_search(arr, first, last):
    while (first <= last):
        mid = (first + last) // 2
        if ele == arr[mid]:
            return f"Found {ele}"
        elif ele < arr[mid]:
            last = mid - 1
        elif ele > arr[mid]:
            first = mid + 1

    return "Not Found"


ele = 7  # element to be searched

print(binary_search(arr_, 0, len(arr_) - 1))
