#!/usr/bin/python
#_*_ coding  UTF-8 _*_

#9 * 9乘法口诀表

for i in range(1, 10):
    j = i
    for j in range(1, 10):
        #print (i, " * ", j, " = ", i * j)
        print ("%d * %d = %d" % (i, j, i * j), end = " || ")
        if (10 > j) and (0 < j):
            j += 1
        pass
    pass
    print ()

