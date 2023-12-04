'''HackerRank
Alphabet Rangoli
https://www.hackerrank.com/challenges/alphabet-rangoli/problem
'''

def print_rangoli(size):
    # your code goes here

    # constraint: 0 < size < 27

    rangoli = []

    # chr 97 is 'a'
    # chr 122 is 'z'

    max_width = None

    # build the bottom half    
    for line_num in range(size):

        # create a rangoli line
        rangoli_line = ''

        # character set

        char_set = [chr(x) for x in range(97 + line_num, 97 + size)]

        # add reversed char_set with char_set without first element to create symmetry
        char_set = char_set[::-1] + char_set[1:]
        
        rangoli_line = '-'.join(char_set)
        if max_width is None:
            max_width = len(rangoli_line)
        rangoli.append(rangoli_line.center(max_width, '-'))
        
        #print(rangoli[-1])
        #print(char_set)
        #print('-'.join(char_set))

    # build the top half by reversing the bottom less the central line
    #rangoli = rangoli[::-1][1:] + rangoli
    rangoli = rangoli[::-1] + rangoli[1:]
    print('\n'.join(rangoli))

   



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)