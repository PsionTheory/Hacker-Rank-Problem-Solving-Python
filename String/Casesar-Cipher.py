#Casesar Cipher
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    l=[]
    alpha="abcdefghijklmnopqrstuvwxyz"
    for i in range(0,len(alpha)):
        l.append(alpha[(i+k)%len(alpha)])
    s1=""
    for i in s:
        if(i in alpha):
            index=ord(i)-97
            s1=s1+l[index]
        elif(i in alpha.upper()):
            index=ord(i)-65
            s1=s1+l[index].upper()
        else:
            s1=s1+i
    return s1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
