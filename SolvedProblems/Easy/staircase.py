#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    staircase = ''
    for i in range(n):
        for j in range(n):
            if j < n - i - 1:
                staircase += ' '
            else:
                staircase += '#'
            if j == n - 1:
                staircase += '\n'
    print(staircase)

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
