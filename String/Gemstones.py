#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gemstones function below.
def unique(arr):  
    G=[]
    for i in arr:
        if i not in G:
            G.append(i)
    return G
def gemstones(arr):
    l=[]
    for j in arr:
        for i in unique(j):
            l.append(i)
    count=0
    v=unique(l)
    for k in v:
        if l.count(k)==len(arr):
            count+=1
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
