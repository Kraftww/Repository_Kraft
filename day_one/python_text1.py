#!/usr/bin/python
# _*_ coding: UTF-8 _*_
input_money = int(input('净利润:'))
arr = [1000000, 600000, 400000, 200000, 100000, 0]
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
current_money = 0
raw_money = input_money
for i in range(0, 6):
    print ("i = ", i)
    if raw_money > arr[i]:
        current_money += (raw_money - arr[i]) * rat[i]
        print ("current_money = ", current_money)
        raw_money = arr[i]
        print ("raw_money = ", raw_money)
pass
print ("最终利润为：", current_money)

