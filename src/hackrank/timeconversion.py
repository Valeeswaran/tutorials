#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    s = s.split(":")
    ap = s[2][2:]

    if ap == "AM":
        if s[0] == "12":
            HH = "00"
        else:
            HH = s[0]

        MM = s[1]
        SS = s[2][:2]
        result = HH + ":" + MM + ":" + SS

        return result

    if ap == "PM":
        if s[0] != "12":
            HH = str(int(s[0]) + 12)
            # HH = HH.rjust(2, "0")
        else:
            HH = s[0]

        MM = s[1]
        SS = s[2][:2]
        result = HH + ":" + MM + ":" + SS

        return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
