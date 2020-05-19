#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    count=0
    i=0
    for i in range(0,len(s),3):
        print(s[i:i+3])
        if s[i:i+3]!="SOS":
            p=s[i:i+3]
            if p[0]!='S':
                count+=1
            if p[1]!='O':
                count+=1
            if p[2]!='S':
                count+=1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
