#!/usr/bin/python
#_*_ coding  UTF-8 _*_

#0 1 1 2 3 5 8 13 21 34 55......
#定义个一个函数
def FirshFunc(n):
    if (1 == n) or (2 == n):
        return 1
    pass
    return FirshFunc(n - 1) + FirshFunc(n - 2)
pass

GetValue = int(input("输入值为："))
if (0 == GetValue):
    print (0)
else:
    print (FirshFunc(GetValue))
#print (FirshFunc(10))
