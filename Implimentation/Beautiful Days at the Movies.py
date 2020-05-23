#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    c=0
    for z in range(i,j+1):
        rev=0
        a=z
        while(z>0):
            dig=z%10
            rev=rev*10+dig
            z=z//10
        if((a-rev)%k==0):
            c+=1
    return(c)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
