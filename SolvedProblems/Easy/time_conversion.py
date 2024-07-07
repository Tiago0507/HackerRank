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
    separate_str = s.split(':')
    new_str = ''
    a_or_p = separate_str[2][2]
    if a_or_p == 'A' and separate_str[0] == '12':
        separate_str[0] = '00'
    elif a_or_p == 'P':
        if separate_str[0] == '01':
            separate_str[0] = '13'
        elif separate_str[0] == '02':
            separate_str[0] = '14'
        elif separate_str[0] == '03':
            separate_str[0] = '15'
        elif separate_str[0] == '04':
            separate_str[0] = '16'
        elif separate_str[0] == '05':
            separate_str[0] = '17'
        elif separate_str[0] == '06':
            separate_str[0] = '18'
        elif separate_str[0] == '07':
            separate_str[0] = '19'
        elif separate_str[0] == '08':
            separate_str[0] = '20'
        elif separate_str[0] == '09':
            separate_str[0] = '21'
        elif separate_str[0] == '10':
            separate_str[0] = '22'
        elif separate_str[0] == '11':
            separate_str[0] = '23'
    separate_str[2] = separate_str[2].replace('A', '').replace('P', '').replace('M', '')
    new_str = ':'.join(separate_str)
    return new_str

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
