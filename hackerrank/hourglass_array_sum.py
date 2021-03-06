#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):

    sum = -sys.maxsize

    for x in range(1, 5):
        for y in range(1, 5):
            sum = max(sum, arr[x-1][y-1]+arr[x-1][y]+arr[x-1][y+1]+arr[x][y]+arr[x+1][y-1]+arr[x+1][y]+arr[x+1][y+1])
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
