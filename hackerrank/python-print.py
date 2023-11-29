'''HackerRank
Python Print
https://www.hackerrank.com/challenges/python-print/problem
'''

if __name__ == '__main__':
    n = int(input())

    # Solution below; Complexity: O(n).

    # constraint - do not use any string methods
    for i in range(1, n+1):
        print(i, end="")
    