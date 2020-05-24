#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    l=len(p)
    r=[]
    for i in range(0,l):
        a=0
        for j in range(0,l):
            if p[j]==(i+1):
                a=j+1
                break
        for j in p:
            if j==a:
                a=p.index(a)
                break
        r.append(a+1)
    return(r)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
