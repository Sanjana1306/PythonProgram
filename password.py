#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    c=0
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    if (n!=6):
        if (n<6):
            return 6-n
        else:
            if any(c in special_characters for c in password):
                pass
            else:
                c=+1
            if any(c in numbers for c in password):
                pass
            else:
                c=+1
            if any(c in lower_case for c in password):
                pass
            else:
                c=+1
            if any(c in upper_case for c in password):
                pass
            else:
                c=+1
            
        return c
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
