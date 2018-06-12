'''
    比C语言的数组强大的地方在于列表中的元素可以是不同类型的:
'''
testList = [1, 'a']
list1 = []
list2 = list()
#print(list2)
# !/usr/bin/python
# -*-coding:utf-8-*-

namelist = ["Edward", "Smith", "John", "Obama", "Polly"]

# 打印方式一
print(namelist[0], end=" ")
print(namelist[1], end=" ")
print(namelist[2], end=" ")
print(namelist[3], end=" ")
print(namelist[4], end=" ")
print()
print("---------------")

# for循环方式
for name in namelist:
    print(name, end=" ")

print()
print("---------------")

# while循环方式
index = 0
while index < len(namelist):
    print(namelist[index], end=" ")
    index += 1
print()
print("---------------")
