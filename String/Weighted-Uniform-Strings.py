#!/bin/python3

import os
import random
import sys

# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    w = set()
    prev = -1
    l = 0
    for c in s:
        x = ord(c) - ord('a') + 1
        w.add(x)
        if prev == c:
            l += 1
            w.add(l*x)
        else:
            prev = c
            l = 1
     
    ans = []
    for q in queries:
        if q in w:
            ans.append("Yes")
        else:
            ans.append("No")
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
