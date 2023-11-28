''' HackerRank
Python If-Else
https://www.hackerrank.com/challenges/py-if-else/problem
'''

# imports specified by hackerrank
import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())

    '''
    Solution below; Complexity: O(1).
    '''

    #constraint 1 <= n < = 100
    if n % 2 == 1:
        print("Weird")
    elif n < 6: # catch even, between 2 and 5 inclusive
        print("Not Weird")
    elif n < 21: # catch even, between 6 and 20 inclusive
        print("Weird")
    else: # catch even, greater than 20
        print("Not Weird")