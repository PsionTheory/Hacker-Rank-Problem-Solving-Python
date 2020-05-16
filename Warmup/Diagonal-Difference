#Diagonal Difference
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    sum1=0
    sum2=0
    for i in range(0,len(arr)):
        for j in range(0,len(arr[i])):
            #print(i,j)
            if i==j:
                sum1+=arr[i][j]
                #if i==int(len(arr)/2):
                #    sum2+=arr[i][j]
            if (i+j)==len(arr)-1: #i=1 j=3, i==j i=3 j=1
                sum2+=arr[i][j]
                #print(arr[i][j])
    return abs(sum1-sum2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
