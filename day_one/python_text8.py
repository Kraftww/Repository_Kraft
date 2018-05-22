#!/usr/bin/python
#_*_ coding  UTF-8 _*_
#使用time模块并格式化输出时间
import time

#TestDict = { 0x0 : "name", 0x1 : "key"}
TestDict = { "name" : 0x0, "key" : 0x1}
for name, key in dict.items(TestDict):
    time.sleep(1)
    print ("One = ", name, "Two =", key)
    print (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
