#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    s=s.lower()
    flag=0
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if i not in s:
            flag=1
            break
    if flag==1:
        return 'not pangram'
    else:
        return 'pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
