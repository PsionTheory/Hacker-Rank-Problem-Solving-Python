#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    flag=0
    for i in range(0,len(s)-1):
        if s[i]==s[i+1]:
            flag=1
            s=s[:i]+s[i+2:]
            break
    if(flag==1):
        s=superReducedString(s)
        if(flag==0):
            return s
    else:
        if s=="":
            fptr.write("Empty String"+ '\n')
        else:
            fptr.write(s+'\n')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    superReducedString(s)
    
    #fptr.write(result + '\n')

    fptr.close()
