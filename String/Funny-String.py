#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    r=s[::-1]
    l1=[ord(i) for i in r]
    l2=[ord(j) for j in s]
    l3= [ abs(l1[i+1]-l1[i]) for i in range(0,len(l1)-2)]
    l4= [ abs(l2[i+1]-l2[i]) for i in range(0,len(l2)-2)]
    for i,j in zip(l3,l4):
        if i!=j:
            return "Not Funny"
    return "Funny"
    #for i,j in r,s:
    #   l1.append(ord(i))
    #  l2.append(ord(j))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
