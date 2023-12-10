'''HackerRank
Maximize It!
https://www.hackerrank.com/challenges/maximize-it/problem
'''


# note: the instructions specifically mention that you don't necessarily need to choose the largest value from each list
# however, I see no reason why you wouldn't to maximize the output

test_input = '''7 867
7 6429964 4173738 9941618 2744666 5392018 5813128 9452095
7 6517823 4135421 6418713 9924958 9370532 7940650 2027017
7 1506500 3460933 1550284 3679489 4538773 5216621 5645660
7 7443563 5181142 8804416 8726696 5358847 7155276 4433125
7 2230555 3920370 7851992 1176871 610460 309961 3921536
7 8518829 8639441 3373630 5036651 5291213 2308694 7477960
7 7178097 249343 9504976 8684596 6226627 1055259 4880436'''



# get modulo and number of lists
#list_count, modulo = input().split()

list_count, modulo = test_input.split('\n')[0].split()


# for each list, get the max and add squared value to total
total = 0
for i in range(int(list_count)):
    #list = [int(x) for x in input().split()]
    list = [int(x) for x in test_input.splitlines()[i+1].split()]
    print(f'{max(list)} >> {list}')
    total += max(list)**2

# print total % modulo
print(f'{total} % {modulo}')
print(total % int(modulo))



