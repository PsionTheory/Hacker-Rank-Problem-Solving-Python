#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    min_len = min(len(s), len(t))
    first_different_index = min_len

    for i in range(min_len):
        if s[i] != t[i]:
            first_different_index = i
            break

    necessary_operations = len(s) + len(t) - 2 * first_different_index

    return("Yes" if k == necessary_operations or (k >= necessary_operations and (k - necessary_operations) % 2 == 0 ) or k >= len(s) + len(t) else "No")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
