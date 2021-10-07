import math
import os
import random
import re
import sys

def camelcase(s):
   c=0
   for i in range(len(s)):
       if (s[i].isupper()==True):
           c=c+1
   return c
        
if __name__ == '__main__':
    
    s = input()
    result = print(camelcase(s))

   