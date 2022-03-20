#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    p = 0
    n = 0
    z = 0
    for a in arr:
        if a < 0:
            n += 1
        if a == 0:
            z += 1
        if a > 0:
            p += 1

    p = p / len(arr)
    n = n / len(arr)
    z = z / len(arr)
    print("{0:.6f}".format(p))
    print("{0:.6f}".format(n))
    print("{0:.6f}".format(z))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
