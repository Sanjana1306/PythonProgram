import re
    
def minimumNumber(n, s):
    c=0
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+" 
    
    for i in s:
        if i.islower():
            break
        else:
            c=c+1
    
    for i in s:
        if i.isupper():
            break
        else:
            c=c+1
    

    for i in s:
        if i.isnumeric():
            break
        else:
            c=c+1
    
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 

    if(regex.search(s) == None):
        pass
    else:
        c=c+1

    
    return c
if __name__ == '__main__':
    global c
    c=0
    n = int(input().strip())
    password = input()
    answer = minimumNumber(n, password)
    print(answer)