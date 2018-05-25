#!/usr/bin/python
# -*- coding: UTF-8 -*-

from functools import reduce

def TextPrint(TextString):
    print("Test String is : %s" % TextString)
    return
pass

def SnAppend(Num, a):
    Tn = 0
    Sn = []
    for count in range(Num):
        Tn = Tn + a
        a = a * 10
        Sn.append(Tn)
        print (Tn)

    Sn = reduce(lambda x, y: x + y, Sn)
    print ("计算和为：%d" % Sn)
    return
pass

