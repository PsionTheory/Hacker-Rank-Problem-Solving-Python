#!/bin/python3

import os
import sys
# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    n = len(s) 
    d = dict() 
    for i in range(n): 
        sub = '' 
        for j in range(i, n): 
            sub = ''.join(sorted(sub + s[j])) 
            d[sub] = d.get(sub, 0) 
            d[sub] += 1
    count = 0
    for k, v in d.items(): 
        count += (v*(v-1))//2
    return count 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
