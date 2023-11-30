'''HackerRank
Validating UID
https://www.hackerrank.com/challenges/validating-uid/problem
'''

uid_count = int(input())

# might as well just process each uid as it is input
for uid in range(uid_count):
    uid = input()

    # quick check to avoid looping
    if len(uid) != 10:
        print('Invalid')
        continue

    # quick check to avoid looping
    if not uid.isalnum():
        print('Invalid')
        continue

    # check for repition
    if len(set(uid)) != len(uid):
        print('Invalid')
        continue

    # count statistics
    uppercase_count = 0
    digit_count = 0
    
    
    for char in uid:
        if char.isupper():
            uppercase_count += 1
        if char.isdigit():
            digit_count += 1

    # checks
    if uppercase_count < 3:
        print('Invalid')
        continue
    
    if digit_count < 3:
        print('Invalid')
        continue

    print('Valid')
    

