#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    vmin=vmax=scores[0]
    maxc=minc=0
    for i in range(1,len(scores)):
        if scores[i]>vmax:
            vmax=scores[i]
            maxc+=1
        if scores[i]<vmin:
            vmin=scores[i]
            minc+=1
    return(maxc,minc)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
