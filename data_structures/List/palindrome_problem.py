# Checks if the given word is palindrome or not
# Line complexity is O(N) Linear as it goes through every item to swap 

def reverse_string(word):
    #converting string to list
    arr = list(word)
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
    return "".join(arr)

def is_palindrome(word):
    if reverse_string(word) == word:
        return True
    return False

print(is_palindrome("radar"))
print(is_palindrome("malayalam"))
print(is_palindrome("madame"))