def binary_search(arr,key):
    left=0
    right=len(arr)-1
    while left <= right:
        mid=(left+right)//2
        if arr[mid] == key:
            return True
        elif arr[mid] < key:
            right=mid-1
        else:
            left=mid+1
    return False


arr=[12,23,34,45,56,67,78,89,90]
key=56
result=binary_search(arr,key)
print("Result : ",result)