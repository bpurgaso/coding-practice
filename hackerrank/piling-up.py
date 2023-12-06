'''HackerRank
Piling Up
https://www.hackerrank.com/challenges/piling-up/problem
'''

# the side length for each cube must be smaller than the one it is on top of
# tl;dr: the side length must be strictly decreasing

# each test case is TWO lines
test_cases = int(input())

for _ in range(test_cases):
    # number of cubes
    cube_count = int(input())
    # side lengths of cubes
    cubes = [int(x) for x in input().split()]


    # get setup for the loop
    if cubes[0] > cubes[-1]:
        cube = cubes.pop(0)
    else:
        cube = cubes.pop(-1)
    
    # conduct the test
    while len(cubes) > 0:
        # pick left or right; popping largest
        
        if (max(cubes[0], cubes[-1]) <= cube):
            if cubes[0] > cubes[-1]:
                cube = cubes.pop(0)
            else:
                cube = cubes.pop(-1)
        else:
            print("No")
            break
    else:
        print("Yes")

        





