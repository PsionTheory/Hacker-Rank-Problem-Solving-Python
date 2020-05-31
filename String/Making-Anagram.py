#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    s11=[i for i in s1]
    s22=[i for i in s2]
    count=0
    for i in range(0,len(s11)):
        if s11[i] in s22:
            s22.remove(s11[i])
            count+=1
    return int(len(s11)+len(s22))-count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
