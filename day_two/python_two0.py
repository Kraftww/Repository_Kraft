#!/usr/bin/python
# -*- coding: UTF-8 -*-

from math import sqrt
from sys import stdout
leap = 1
h = 0
for m in range(2, 201):
    k = int(sqrt(m + 1))
    print (leap)
    for i in range(2,k + 1):
        if (m % i == 0):
            leap = 0
            break
    pass
    if (leap == 1):
        print ('%-4d' % m)
        h += 1
        if (h % 10 == 0):
            print ('')
    leap = 1
print ('The total is %d' % h)