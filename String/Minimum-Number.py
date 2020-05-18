#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    flag=[False,False,False,False]        
    for i in password:
        if i in numbers:
            flag[0]=True
        if i in lower_case:
            flag[1]=True
        if i in upper_case:
            flag[2]=True
        if i in special_characters:
            flag[3]=True
    count=0 
    for i in flag:
        if i==False:
            count+=1
    if n<6:
        return max(6-n,count)
    else:
        return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
