#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the anagram function below.
def anagram(s):
    if len(s)%2==1:
        return -1
    else:
        z=int(len(s)/2)
        s1=s[:z]
        s2=s[z:]
        s11=[i for i in s1]
        s22=[i for i in s2]
        
        count=0
        for i in range(0,z):
            if s11[i] not in s22:
                count+=1
            else:
                s22.remove(s11[i])
        return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
