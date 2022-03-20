#!/bin/python

import math
import os
import random
import re
import sys


def check_odd_even(n):
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and n >= 2 and n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and n >= 6 and n <= 20:
        print("Weird")
    elif n % 2 == 0 and n >= 20:
        print("Not Weird")


def raw_input():
    n = input("Enter number: ")
    return n


if __name__ == '__main__':
    n = int(raw_input().strip())
    check_odd_even(n)