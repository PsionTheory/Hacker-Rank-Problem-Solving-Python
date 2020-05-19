#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    ns=[]
    for i in alice:
        scores.append(i)
        scores.sort(reverse=True)
        ind=scores.index(i)
        r=1
        for j in range(0,ind):
            if scores[j]!=scores[j+1]:
                r+=1
        ns.append(r)
    return(ns)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
