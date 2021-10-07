'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def fibonacci(num):
    a=0
    b=1
    next=0
    for i in range(1,num+1,2):
        next=a+b
        a=b
        b=next
    print(a)

def prime(num):
    for i in range(2,num+1):
        if i>1:
            for j in range(2,i):
                if (i%j==0):
                    break
        else:
            print(i)
            
    
    
n=int(input("Enter the position"))
if (n%2!=0):
    fibonacci(n)
else:
    prime(n//2)
    
