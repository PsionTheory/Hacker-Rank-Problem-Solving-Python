#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    r=s[::-1]
    count=0
    sum=0
    if len(s)%2==1:
        z=1
    else:
        z=0
    z+=int(len(s)/2)
    for i,j in zip(r,s):
        if(count==z):
            break
        sum+=abs(ord(i)-ord(j))
        count+=1
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
