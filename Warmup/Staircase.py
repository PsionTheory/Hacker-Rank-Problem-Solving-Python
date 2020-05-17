#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    k = n-1
  
    # outer loop to handle number of rows 
    for i in range(0, n): 
        str1=""
        # inner loop to handle number spaces 
        # values changing acc. to requirement 
        for j in range(0, k): 
            str1=str1+" "#print() 
      
        # decrementing k after each loop 
        k = k - 1
      
        # inner loop to handle number of columns 
        # values changing acc. to outer loop 
        str2=""
        for j in range(0, i+1): 
            str2=str2+"#" 
      
        # printing line after each row 
        print(str1+str2) 
if __name__ == '__main__':
    n = int(input())

    staircase(n)
