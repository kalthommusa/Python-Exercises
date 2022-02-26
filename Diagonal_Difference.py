#!/bin/python

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
    # Write your code here

    primary_diagonal = 0
    secondary_diagonal = 0
    n = len(arr)


    for i in range(n):
        # calculate sum of primary diagonal
        primary_diagonal += arr[i][i]
        # calculate sum of secondary diagonal
        secondary_diagonal += arr[i][n-1-i]

    print("The primary diagonal is: {}".format(primary_diagonal))
    print("The secondary diagonal is: {}".format(secondary_diagonal))
               
    # calculate the difference of the sums
    difference = abs(primary_diagonal - secondary_diagonal)
    return difference

       

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    arr = []

    for _ in xrange(n):
        arr.append(map(int, raw_input().rstrip().split()))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
    
