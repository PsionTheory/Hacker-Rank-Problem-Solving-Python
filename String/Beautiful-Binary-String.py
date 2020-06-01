#!/bin/python3

import os
import sys


# Complete the beautifulBinaryString function below.
def repl(s,position,replacement):
    return s[:position] + replacement + s[position+1:]
def beautifulBinaryString(b):
    count=0
    if b.find('010')==-1:
        return 0
    else:
        i=0
        x=len(b)-3
        while(i<=x):
            if b[i]=='0'and b[i+1]=='1' and b[i+2]=='0':
                b=repl( b ,i+2,'1')
                count+=1
                i+=3
            elif b[i]=='0'and b[i+1]=='1':
                i+=2
            else:
                i+=1
        return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
