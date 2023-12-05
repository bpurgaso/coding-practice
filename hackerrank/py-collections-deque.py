'''HackerRank
py collections deque
https://www.hackerrank.com/challenges/py-collections-deque/problem
'''

from collections import deque


if __name__ == '__main__':
    line_count = int(input())
    d = deque()

    for _ in range(line_count):
        command = input().split()

        if command[0] == 'append':
            d.append(command[1])
        elif command[0] == 'appendleft':
            d.appendleft(command[1])
        elif command[0] == 'pop':
            d.pop()
        elif command[0] == 'popleft':
            d.popleft()
        else:
            raise ValueError('Invalid command')
        
    print(' '.join(d))