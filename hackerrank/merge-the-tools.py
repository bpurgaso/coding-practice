'''HackerRank
Merge the Tools
https://www.hackerrank.com/challenges/merge-the-tools/problem
'''

def merge_the_tools(string, k):
    # your code goes here

    '''
    1. subdivide string into k length substrings
    2. remove duplicate characters from each substring
    3. print each substring on a new line
    '''

    #constraint: k is a factor of n; n is the length of string
    for i in range(0, len(string), k):
        substring = string[i:i+k]
        print(''.join(set(substring)))

if __name__ == '__main__':
    #string, k = input(), int(input())
    string, k = 'AABCAAADA', 3
    merge_the_tools(string, k)

