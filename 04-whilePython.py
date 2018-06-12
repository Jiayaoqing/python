#!/usr/bin/python
# -*- coding:utf-8 -*-

import random

# 初始化用户名字
name = input("请输入您的名字:\n")
# 初始化账户100块钱
acount = 100

print("\t拉斯维加斯世界赌王争霸赛\t")
print("比赛正式开始...\n")
while acount > 0:
    # 输入本次押注的金额
    money = input("请输入压住金额:")
    # 判断用户账户余额是否够押注
    if int(money) > acount:
        print("余额不足,请重新押注!\n")
        print("您的余额:%d\n" % (acount))
    else:
        # 输入押注的数字
        number = input("请输入押注数字(1-10):")
        # 检测押注数字是否在1-10
        if int(number) > 0 and int(number) <= 10:
            # 开盅
            dice = random.randint(1, 2)
            print("本次开盅数字为:%d,您押注的数字为:%s\n" % (dice, number))
            if int(number) == dice:
                print("恭喜您,本轮押注胜利,获得返还金额:%d" % (int(money) * 2))
                acount = acount + int(money) * 2
            else:
                acount = acount - int(money)
                print("很遗憾,本轮押注失败,余额为:%d" % (acount))
        else:
            print("押注数字应该在1-10,请重新输入:)\n")

print("Game Over!")
