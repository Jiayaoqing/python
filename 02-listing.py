#!/usr/bin/python
# -*-coding:utf-8-*-

import random

# 创建办公室列表
offices = [[], [], []]

# 员工列表
workers = []
# 初始化员工列表
nameID = "ABCDEFGH"
index = 0;
while index < 8:
    # 员工姓名
    name = "员工"
    name += nameID[index]
    # print(name)
    workers.append(name)    # append() 方法用于在列表末尾添加新的对象。
    index += 1

# 随机分配员工
for name in workers:
    # 随机产生办公室编号
    officeID = random.randint(0, 2)
    # 将当前员工分配到办公室中
    offices[officeID].append(name)

# 输出各个办公室人员列表
for work_list in offices:
    print("当前办公室员工人数:%d" % len(work_list))
    for person in work_list:
        print(person)
