'''HackerRank
Matrix Script
https://www.hackerrank.com/challenges/matrix-script/problem
'''

import re

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

# create 2d array
matrix = [['' for x in range(m)] for y in range(n)]

for i in range(n):
    line = input()
    count = 0    
    for char in line:
        #print(f'i: {i}, count: {count}, char: {char}')
        matrix[i][count] = char
        count += 1

output = ''
for i in range(m):
    for j in range(n):
        output += matrix[j][i]

print(re.sub(r'([a-zA-Z0-9])[^a-zA-Z0-9]+([a-zA-Z0-9])', r'\1 \2', output))
