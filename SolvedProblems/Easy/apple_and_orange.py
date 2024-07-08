#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    num_of_apples_in_the_house = 0
    num_of_oranges_in_the_house = 0
    for index, apple in enumerate(apples):
        apples[index] = a + apple
        if apples[index] in range(s, t + 1):
            num_of_apples_in_the_house += 1
    for index, orange in enumerate(oranges):
        oranges[index] = b + orange
        if oranges[index] in range(s, t + 1):
            num_of_oranges_in_the_house += 1
    print(f'{num_of_apples_in_the_house}\n{num_of_oranges_in_the_house}')        

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
