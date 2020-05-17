#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    max1=max(arr)
    min1=min(arr)
    arr.remove(min1)
    max_sum=sum(arr)
    arr.remove(max1)
    min_sum=sum(arr)+min1
    print(min_sum, max_sum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
