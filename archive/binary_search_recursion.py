# this code will search for a integer in a sorted list using recursion

arr_ = [1, 1, 2, 3, 3, 3, 4, 5, 6, 7]


def binary_search(arr, first, last):
    if first > last:
        return "Not Found"
    else:
        mid = (first + last) // 2
        if arr[mid] == ele:
            return f"Found {ele}"
        elif arr[mid] > ele:
            print (arr, first, mid - 1)
            return binary_search(arr, first, mid - 1)
        elif arr[mid] < ele:
            print (arr, mid + 1, last)
            return binary_search(arr, mid + 1, last)


ele = 7  # element to be searched
print(binary_search(arr_, 0, len(arr_) - 1))
