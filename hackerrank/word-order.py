'''HackerRank
Word Order
https://www.hackerrank.com/challenges/word-order/problem
'''



line_count = int(input())

# assumption: keys in a dictionary are ordered
count = {}
for _ in range(line_count):
    # assume one word per line
    word = input()
    if word not in count.keys():
        count[word] = 1
    else:
        count[word] += 1

print(len(count.keys()))
print(' '.join([str(x) for x in count.values()]))