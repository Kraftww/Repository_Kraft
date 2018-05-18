#!/usr/bin/python
# _*_ coding: UTF-8 _*_
a = 0
b = 0
c = 0
AddNum = 0
for i in range(1, 5):
    a = i
    for j in range(1, 5):
        if ( a != j ):
            b = j
            for k in range(1, 5):
                if (a != k) and (b != k):
                    c = k
                    print (a, b, c)
                    AddNum += 1
pass
print("非重复数量为：", AddNum)


