x=[]
z=[]
y=[]
str_=[]
count=0
#str_=input("Enter the string")
str_=input(list(map(lambda i:i,str_)))


for i in range(0,len(str_)):
    for j in range (i+1,len(str_)+1):
        x=str_[i:j]
        print(str_[i:j],end=",")
    #print(list(x))

for i in range(0,len(x)):
    #for j in range (i+1,len(x)+1):
        if (x[i]=='a' or x[i]=='e' or x[i]=='i' or x[i]=='o' or x[i]=='u'):
            print(x[i:j],end=",")
            #print(z)
        else:
            y=x[i]
            print(y)

