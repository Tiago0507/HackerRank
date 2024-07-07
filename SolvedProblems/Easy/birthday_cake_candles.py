#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    tallest_candle = candles[0]
    num_tallest_candle = 0
    for candle in candles:
        if candle > tallest_candle:
            tallest_candle = candle
            num_tallest_candle = 1
        elif candle == tallest_candle:
            num_tallest_candle += 1
    return num_tallest_candle

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
