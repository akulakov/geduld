#!/usr/bin/env python3
from textdistance import hamming
for l in open('temp.txt'):
    a,b=l.split(' - ')
    if not a.startswith('1'):
        b = b.split()[-1]
        if hamming.distance(a,b) <= 2:
            print('1 ' + l, end='')
            continue
    print(l, end='')



