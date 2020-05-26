#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def checkalt(s1):
    c1=s1[0]
    for i in range(0,len(s1)):
        if i%2==0:
            if s1[i]!=c1:
                return False
        if i%2==1:
            if s1[i]==c1:
                return False
    return True
def toggle_find(find):
    if find==65:
        find=66
    elif find==66:
        find=65
    return find

def a(i):
    count=0
    l=[ord(i1) for i1 in i]
    find=ord(i[0])
    for i in range(0,len(l)):#dont allow the first casw to go in
        if l[i]==find:
            find=toggle_find(find)
        else:
            count+=1
    return count

def alternatingCharacters(s):
    i=s
    if 'B' not in i:
        return len(i)-1
    elif 'A' not in i:
        return len(i)-1
    elif(checkalt(i)):
        return 0
    else:
        return a(i)
    return 0



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
