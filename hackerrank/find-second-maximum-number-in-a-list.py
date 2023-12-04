'''HackerRank
Find the Runner-Up Score!
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
'''

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = sorted(set(arr))
    
    print(arr[-2])