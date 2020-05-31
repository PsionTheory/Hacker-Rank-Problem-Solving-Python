#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def checkPalindrome(s):
    r=s[::-1]
    if len(s)%2==1:
        z=1
    else:
        z=0
    z+=int(len(s)/2)
    for i in range(0,z):
        if r[i]!=s[i]:
            return False
    return True
    
def palindromeIndex(s):
    r=s[::-1]
    if len(s)%2==1:
        z=1
    else:
        z=0
    z+=int(len(s)/2)
    for i in range(0,z):
        if r[i]!=s[i]:
            if(checkPalindrome(s[:i]+s[i+1:])):
                return i
            elif(checkPalindrome(r[:i]+r[i+1:])):
                return len(s)-1-i
            else:
                return -1
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
