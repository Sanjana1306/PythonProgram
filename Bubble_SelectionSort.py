ar=[12,1,5,10,6]
n=len(ar)
#BubbleSort
for i in range(n):
    for j in range(i+1,n):
        if ar[i]>ar[j]:
            ar[i],ar[j]=ar[j],ar[i]



#Selection_Sort
'''for i in range(n):
    min=i
    for j in range(i+1,n):
        if ar[j]<ar[min] :
            min=j
    
    ar[i],ar[min]=ar[min],ar[i]'''
    
for i in range(n):
    print(ar[i])