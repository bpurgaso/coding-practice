'''HackerRank
Most Commons
https://www.hackerrank.com/challenges/most-commons/problem
'''

from collections import Counter


# sorted is required because Counter returns equal occurrences in the order they were first seen
company_name = Counter(sorted(input()))


print('\n'.join([f'{x[0]} {x[1]}' for x in company_name.most_common(3)]))


