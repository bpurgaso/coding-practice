'''HackerRank
Python String Formatting
https://www.hackerrank.com/challenges/python-string-formatting/problem
'''



def print_formatted(number):
    # your code goes here

    # -2 because of the 0b prefix on binary numbers
    width = len(bin(number)) - 2
    #print(f':{bin(width)}:')
    #print(f':{width}:')

    for i in range(1, n + 1):
        print(f'{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}')


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)