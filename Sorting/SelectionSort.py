def Selection_Sort(arr):
    n=len(arr)
    for i in range(0,n-1):
        min=i
        for j in range(i+1,n):    
            if arr[min]>arr[j]:
                min=j
        if min != i:
            temp=arr[min]
            arr[min]=arr[i]
            arr[i]=temp
    print(arr)
    
arr=[23,12,43,57,87,43,64,32]
print(arr)
print("After Sorting")
Selection_Sort(arr)
