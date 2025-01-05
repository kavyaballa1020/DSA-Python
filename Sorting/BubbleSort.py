def bubble_sort(arr):
    n=len(arr)
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return arr
    
arr=[23,43,65,12,76,89,67,32]
print(bubble_sort(arr))