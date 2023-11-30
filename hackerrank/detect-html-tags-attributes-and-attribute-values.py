'''HackerRank
Detect HTML tags, attributes and attribute values
https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem
'''

from pprint import pprint as pp
from bs4 import BeautifulSoup



line_count = int(input())
raw_html = ''

for _ in range(line_count):
    raw_html += f'{input()}\n'


# use the first line's line-count specification to limit the input
html_lines = raw_html.splitlines()
html = '\n'.join(html_lines[:line_count])

soup = BeautifulSoup(html, 'html.parser')

# Get all tags, filtering out comments
tags = [tag for tag in soup.find_all() if not tag.is_comment]

for tag in tags:
    print(tag.name)
    for attribute in tag.attrs:
        if isinstance(tag[attribute], list):
            print(f'-> {attribute} > {" ".join(tag[attribute])}')
        else:
          print(f'-> {attribute} > {tag[attribute]}')

