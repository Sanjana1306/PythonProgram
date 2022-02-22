def Merge(arr,l,q,r):
    n1=q-l+1
    n2=r-q
    L=[]
    R=[]
    for i in range(n1):
        L[i]=arr[l+i]
    
    for j in range(n2):
        R[j]=arr[q+j]
    
    
    for i in range(n1):
        for j in range(n2):
            while i<n1 and j<n2:
                if L[i]<R[j]:
                    arr[k]=L[i]
                    i=i+1
                else:
                    arr[k]=R[j]
                    j=j+1
                k=k+1
            
    while i<len[L]:
        arr[k]=L[i]
        i+=1
        k+=1
    while j<len[R]:
        arr[k]=R[j]
        j+=1
        k+=1

def mergesort(arr,l,r):
    if l<r:
        q=(l+r)/2
        mergesort(arr,l,q)
        mergesort(arr,q+1,r)
        Merge(arr,l,q,r)
    


arr=[1,12,5,46,7,9,8]
n=len(arr)
mergesort(arr,0,n)
for i in range(len(arr)):
    print(arr[i])
   
    
    

