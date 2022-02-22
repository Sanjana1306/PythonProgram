def partition(arr,low,high):
    i=low-1
    pivot=arr[high]
    for j in range(low,high):
        if arr[j]<pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
            
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
        


def QuickSort(arr,p,r):
    if p<r:
        q=partition(arr,p,r)
        QuickSort(arr,p,q-1)
        QuickSort(arr,q+1,r)




#arr =[1,21,5,7,8,10,56,2]
#n=len(arr)
arr=[]
n = int(input(("Enter the size of an array"))
arr = list(map(int, input().strip().split()))
QuickSort(arr,0,n-1)
print("Sorted Array")
for i in range(n):
    print(arr[i])
    
    
    
