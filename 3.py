import re

pattern = re.compile('.*ERROR.*')
with open('2.csv', 'r') as f:
    for line in f.readlines():
        if pattern.match(line):
            print(line)