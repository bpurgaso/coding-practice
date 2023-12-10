'''HackerRank
Maximize It!
https://www.hackerrank.com/challenges/maximize-it/problem
'''


# I originally misread the instructions. You are not trying to find the largest product, you're trying to find the largest remainder after the modulus operation

from itertools import product

list_count, modulo = input().split()

squared_lists = []
for i in range(int(list_count)):
    squared_lists.append([int(x)**2 for x in input().split()[1:]])

products = [sum(x) % int(modulo) for x in product(*squared_lists)]
print(max(products))
