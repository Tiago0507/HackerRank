# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import atan, degrees

def find_angle(AB, BC):
    tang = AB / BC
    angle = round(degrees(atan(tang)))
    return f'{angle}{chr(176)}'

AB = int(input())
BC = int(input())

print(find_angle(AB, BC))