'''HackerRank
Validating Credit Card Numbers
https://www.hackerrank.com/challenges/validating-credit-card-number/problem
'''

# I had one problem, then I decided to use regex
# Now I have two problems.

import re

regex = re.compile(r'^[456]\d{3}(-?)\d{4}(-?)\d{4}(-?)\d{4}$')
regex_duplicates = re.compile(r'(\d)\1{3}')

cc_count = int(input())
#print(cc)

for _ in range(cc_count):
    cc = input()
    if regex.match(cc) and not regex_duplicates.search(cc.replace('-', '')):
        print('Valid')
    else:
        print('Invalid')