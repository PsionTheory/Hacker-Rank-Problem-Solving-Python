#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    l=s.split(":")
    hour=l[0]
    minute=l[1]
    second=l[2][:2]
    ampm=l[2][2:]
    if ampm=="AM":
        if int(hour)!=12:
            hours=hour
        else:
            hours="00"
    else:
        if int(hour)!=12:
            hours=int(hour)+12
        else:
            hours=int(hour)
    return str(hours)+":"+str(minute)+":"+str(second)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
