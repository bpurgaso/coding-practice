'''HackerRank
The Minion Game
https://www.hackerrank.com/challenges/the-minion-game/problem
'''

from collections import defaultdict

def minion_game(string):
    # your code goes here

    '''
    1. compute all substrings; storing in a tree structure
    3. compute score for each player by only traversing trees with AEIOU roots for Kevin and others for Stuart
    4. print winner and score
    '''


    # compute all substrings, storing in a dict
    substrings = defaultdict(int)
    length = len(string)

    # to deal with excessively long inputs, had to move to a single pass method replacing the inner loop with the "count" variable
    for i in range(len(string)):
        count = length - i
        # we don't actually care about the substrings, just their first character for assignment purposes and frequency
        # to reduce memory pressure we discard all substrings, only tracking the first character and count
        substrings[string[i]] = substrings[string[i]] + count
            
    # compute score for each player
    kevin_score = 0
    stuart_score = 0

    for key in substrings.keys():
        if key[0] in "AEIOU":
            kevin_score += substrings[key]
        else:
            stuart_score += substrings[key]

    # print winner and score
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")

if __name__ == '__main__':
    #s = input()
    s = "BANANA"
    minion_game(s)