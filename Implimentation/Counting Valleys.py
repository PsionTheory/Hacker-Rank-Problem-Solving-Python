#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    c=0
    t=0
    for i in s:
        pc=c
        if i=='U':
            c+=1
        else:
            c-=1
        if pc==-1 and c==0:
            t+=1
    return(t)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
