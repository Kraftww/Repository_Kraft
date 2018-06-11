#!/usr/bin/python
# -*- coding: UTF-8 -*-

class JustCounter:

    def __TestPrint(self, TestString):
        print (self.TestString)
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        self.__TestPrint(self.__secretCount)
pass

counter = JustCounter()
counter.count()
counter.count()
print (counter.publicCount)
print (counter.__secretCount)  # 报错，实例不能访问私有变量