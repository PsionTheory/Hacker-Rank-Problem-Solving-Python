#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    b=[]
    for i in range(0,len(a)):
        countl=0
        counth=0
        for j in range(i,len(a)):
            if(a[j]==a[i] or a[j]==a[i]-1):
                countl+=1
            if(a[j]==a[i] or a[j]==a[i]+1):
                counth+=1            
            b.append(max(countl,counth))
    return(max(b))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
