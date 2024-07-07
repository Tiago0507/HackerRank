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
    quantity_pos = 0
    quantity_neg = 0
    quantity_zero = 0
    for num in arr:
        if num > 0:
            quantity_pos += 1
        elif num < 0:
            quantity_neg += 1
        else:
            quantity_zero += 1
    ratio_pos = round(quantity_pos / len(arr), 6)
    ratio_neg = round(quantity_neg / len(arr), 6)
    ratio_zero = round(quantity_zero / len(arr), 6)
    print(f'{ratio_pos}\n{ratio_neg}\n{ratio_zero}')
            
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
