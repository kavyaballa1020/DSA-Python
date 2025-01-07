def Insertion_Sort(arr):
    n=len(arr)
    for i in range(1,n):
        temp=arr[i]
        j=i-1
        while temp<arr[j] and j>=0:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=temp
    print(arr)
arr=[23,12,43,57,87,43,64,32]
print(arr)
print("After Sorting : ")
Insertion_Sort(arr)