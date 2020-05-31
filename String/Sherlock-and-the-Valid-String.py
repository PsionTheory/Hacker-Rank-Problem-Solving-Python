#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    s1=[i for i in s]
    l1=[]
    flag=0
    for i in set(s1):
        l1.append(s1.count(i))
    z=set(l1)
    print(z)
    if len(z)>2:
        return "NO"
    elif len(z)==1:
        return "YES"
    else:
        a=list(z)[0]
        b=list(z)[1]
        if (a>1 and b>1):
            if(abs(a-b)==1):
                x=max(a,b)
                if(l1.count(x)==1):
                    return "YES"
                else:
                    return "NO"
            else:
                return "NO"
        else:
            if l1.count(1)==1:
                return "YES"
            else:
                return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
