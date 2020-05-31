#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    l=[i for i in s]
    if len(l)==1:
        return "YES"
    else:
        l1=[]
        for i in set(l):
            l1.append(l.count(i))
        if len(l)%2==0:
            for i in l1:
                if i%2==1:
                    return "NO"
            return "YES"
        else:
            flag=0
            for i in l1:
                if i%2==1 and flag==0:
                    flag=1
                elif i%2==1 and flag==1:
                    return "NO"
            return "YES"            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
