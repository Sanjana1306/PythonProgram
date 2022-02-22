def mergesort(arr):
    if len(arr)>1:
        r=len(arr)
        q=r//2
        L=arr[:q]
        R=arr[q:]
        
        mergesort(L)
        mergesort(R)
        
        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1
    




'''def mergesort(arr,l,r):
    q=(l+r)/2
    mergesort(arr,l,q)
    mergesort(arr,q+1,r)
    Merge(arr,l,q,r)'''


#arr=[1,12,5,46,7,9,8]
arr=list(map(int,input().strip().split()))
mergesort(arr)
for i in range(len(arr)):
    print(arr[i])
    
    
    
    