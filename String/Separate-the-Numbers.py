#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the separateNumbers function below.
def check(s, mini):
    while s:
        if s.startswith(mini):
            s = s[len(mini):]
            mini = str(int(mini) + 1)
        else:
            return False
    return True
    
def separateNumbers(s):
    for i in range(1, len(s)//2 + 1):
        mini = s[:i]
        if check(str(s), mini):
            return "YES " + mini
    return "NO"

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        print(separateNumbers(s))
