 #Input from the user and converting it to uppercase
s=input("Enter the sentence\n").upper()  
l=['A','E','I','O','U']
#Creating two empty list to store the result
r=[ ]  
k=[ ]
for i in l:
    if i in s:
        r.append(i)               #If vowel is present append in list r
        k.append(s.count(i))      #Appending the count of present vowel
print("Vowels in sentence -",r,"\nEach vowel repeated as -",k)    #Displaying the output
        
