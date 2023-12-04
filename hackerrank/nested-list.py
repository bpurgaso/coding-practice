'''HackerRank
Nested Lists
https://www.hackerrank.com/challenges/nested-list/problem
'''


if __name__ == '__main__':

    name_score_list = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_score_list.append([name, score])
    
    # constraint: there will always be one ore more students with second lowest score

    second_lowest_score = list(set([score for _, score in sorted(name_score_list, key=lambda x: x[1])]))[1]
    #print(f'second_lowest_score: {second_lowest_score}')
    second_lowest_score_names = [name for name, score in sorted(name_score_list, key=lambda x: x[0]) if score == second_lowest_score]
    #print(f'second_lowest_score_names: {second_lowest_score_names}')
    print('\n'.join(second_lowest_score_names))