#!/usr/bin/python
#_*_ coding  UTF-8 _*_

year = int(input('year:\n'))
month = int(input('month:\n'))
day = int(input('day:\n'))

#定义元组数据
months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)

if (month > 0) \
    and (month < len(months)) \
    and (day > 0) \
    and (day < 32):
    GetPutCurNum = months[month - 1] + day
    print (year, "年", month ,"月", day, "日", "是今年的第", GetPutCurNum, "天")
else:
    print ("Input param invalid")
pass
