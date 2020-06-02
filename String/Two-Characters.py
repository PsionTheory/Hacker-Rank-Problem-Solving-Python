#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations 

def is_alternate(s1,a,b):
    s2=[]
    for i in s1:
        if i==a or i==b:
            s2.append(i)
    for i in range(0,len(s2)):
        if i%2==0 and s2[0]!=s2[i]:
            return -1
        if i%2==1 and  s2[1]!=s2[i]:
            return -1
    return len(s2)

# Complete the alternate function below.
def alternate(s):
    s1=[i for i in s]
    perm = permutations(set(s1), 2)
    maxi=0
    for i in perm:
        #print(i)
        z=is_alternate(s1,i[0],i[1])
        if(z!=-1):
            if(z>maxi):
                maxi=z
    return maxi

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
