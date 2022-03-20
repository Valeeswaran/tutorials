#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    l = len(arr)
    i = 0
    j = l-1

    lst = []
    rst = []
    for a in arr:
        for idx, b in enumerate(arr):
            if idx == i:
                lst.append(b[i])
                rst.append(b[j])
        i += 1
        j -= 1

    result = abs(sum([i for i in lst]) - sum([j for j in rst]))
    print(lst, rst, result)

    return result


if __name__ == '__main__':


    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)


