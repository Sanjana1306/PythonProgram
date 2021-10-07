e=[]
o=[]
s=0
x=0
c=0
l=str(input())
char=list(l)
print(char)
for i in range(len(l)):
    if i%2==0:
        e.append(l[i])
    else:
        o.append(l[i])
    
for i in range(0,len(e)):
    s=s+ord(e[i])

for i in range(0,len(o)):
    x=x+ord(o[i])

c=abs(s-x)
    

if(c%3==0 or c%5==0 or c%7==0):
    print("Prime String")
else:
    print("Casual String")