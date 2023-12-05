'''HackerRank
Capitalize
https://www.hackerrank.com/challenges/capitalize/problem
'''


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    # you have to split on spaces explicitly to preserve the count
    # some test cases intentionally add extra spaces between words
    return ' '.join([x.capitalize() for x in s.split(' ')])
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = "chris alan"
    s = input()

    result = solve(s)

    print(result)
    fptr.write(result + '\n')

    fptr.close()
