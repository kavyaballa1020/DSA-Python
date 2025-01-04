def linear_search(arr, key):
    for i in arr:
        if i == key:
            return True
    return False
arr = [23, 54, 53, 76, 61, 97, 73]
key = 97
result = linear_search(arr, key)
print("Element found:", result)  
